import time
import trafilatura
from deep_translator import MyMemoryTranslator

def translate_to_spanish(text: str, max_chars: int = 350) -> str:
    """Translates text from English to Spanish using MyMemory with fallback."""
    if not text:
        return ""
    
    clean_text = text.strip()
    if len(clean_text) > max_chars:
        # Cut cleanly at last space
        cut = clean_text[:max_chars]
        last_sp = cut.rfind(" ")
        if last_sp != -1:
            clean_text = cut[:last_sp]
        else:
            clean_text = cut
            
    try:
        translator = MyMemoryTranslator(source="en-US", target="es-ES")
        translated = translator.translate(clean_text)
        if translated and not translated.startswith("MYMEMORY WARNING:"):
            return translated.strip()
    except Exception as e:
        print(f"⚠️ Translation warning: {e}")
        
    return clean_text

def extract_and_summarize(url: str, default_title: str, default_summary: str) -> dict:
    """
    Visits the article webpage, strips 100% of ads, navigation, and banners,
    extracts the core body paragraphs, and produces a structured 3-bullet Spanish summary.
    """
    print(f"🌐 Extrayendo contenido limpio de: {url}")
    
    title_es = translate_to_spanish(default_title, max_chars=180) or default_title
    
    body_text = None
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            body_text = trafilatura.extract(
                downloaded,
                include_comments=False,
                include_tables=False,
                no_fallback=False
            )
    except Exception as e:
        print(f"⚠️ Trafilatura fetch error on {url}: {e}")

    paragraphs = []
    if body_text:
        # Filter paragraphs with substantial content (ignore small fragments, author tags, etc.)
        raw_paras = [p.strip() for p in body_text.split("\n") if len(p.strip()) > 60]
        # Ignore boilerplate lines
        blacklist = ["cookie", "privacy policy", "all rights reserved", "subscribe", "newsletter", "sign up", "terms of use"]
        for p in raw_paras:
            if not any(b in p.lower() for b in blacklist):
                paragraphs.append(p)
                
    bullets = []
    labels = [
        ("📌 **¿Qué sucedió?**", "¿Qué sucedió?"),
        ("🔍 **Detalles clave**", "Detalles clave"),
        ("💡 **Impacto y contexto**", "Impacto y contexto")
    ]
    
    if len(paragraphs) >= 2:
        # Use top 2-3 clean paragraphs
        chosen = paragraphs[:3]
        for idx, para in enumerate(chosen):
            prefix = labels[idx][0] if idx < len(labels) else "🔹 **Detalle adicional**"
            translated_p = translate_to_spanish(para, max_chars=320)
            bullets.append(f"{prefix}: {translated_p}")
            time.sleep(0.3) # small throttle between calls
    else:
        # Fallback to the RSS summary if the page extraction was blocked
        translated_fallback = translate_to_spanish(default_summary, max_chars=320)
        bullets.append(f"📌 **¿Qué sucedió?**: {translated_fallback}")
        bullets.append("🔍 **Detalles clave**: Consulta el enlace original para leer la cobertura extendida.")

    return {
        "title_es": title_es,
        "title_en": default_title,
        "bullets": bullets,
        "url": url
    }
