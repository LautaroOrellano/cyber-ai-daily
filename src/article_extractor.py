import time
import trafilatura
from deep_translator import MyMemoryTranslator

def translate_to_spanish(text: str, max_chars: int = 350) -> str:
    """Translates text from English to Spanish using MyMemory with fallback."""
    if not text:
        return ""
    
    clean_text = text.strip()
    if len(clean_text) > max_chars:
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

def truncate_clean(text: str, max_chars: int = 320) -> str:
    """Truncates text at the last word cleanly."""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    last_sp = cut.rfind(" ")
    return (cut[:last_sp] if last_sp != -1 else cut) + "..."

def extract_and_summarize(url: str, default_title: str, default_summary: str) -> dict:
    """
    Visits the article webpage, strips 100% of ads, navigation, and banners,
    extracts the core body paragraphs, and produces structured bullet summaries
    in both English (default) and Spanish.
    """
    print(f"🌐 Scraping clean text from: {url}")
    
    title_en = default_title.strip()
    title_es = translate_to_spanish(title_en, max_chars=180) or title_en
    
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
        raw_paras = [p.strip() for p in body_text.split("\n") if len(p.strip()) > 60]
        blacklist = ["cookie", "privacy policy", "all rights reserved", "subscribe", "newsletter", "sign up", "terms of use"]
        for p in raw_paras:
            if not any(b in p.lower() for b in blacklist):
                paragraphs.append(p)
                
    bullets_en = []
    bullets_es = []
    
    labels_en = [
        "📌 **What happened?**",
        "🔍 **Key details**",
        "💡 **Context & Impact**"
    ]
    labels_es = [
        "📌 **¿Qué sucedió?**",
        "🔍 **Detalles clave**",
        "💡 **Impacto y contexto**"
    ]
    
    if len(paragraphs) >= 2:
        chosen = paragraphs[:3]
        for idx, para in enumerate(chosen):
            lbl_en = labels_en[idx] if idx < len(labels_en) else "🔹 **Additional detail**"
            lbl_es = labels_es[idx] if idx < len(labels_es) else "🔹 **Detalle adicional**"
            
            clean_en = truncate_clean(para, max_chars=320)
            bullets_en.append(f"{lbl_en}: {clean_en}")
            
            trans_es = translate_to_spanish(para, max_chars=320)
            bullets_es.append(f"{lbl_es}: {trans_es}")
            time.sleep(0.3)
    else:
        clean_fallback_en = truncate_clean(default_summary, max_chars=320)
        bullets_en.append(f"📌 **What happened?**: {clean_fallback_en}")
        bullets_en.append("🔍 **Key details**: Read the full original coverage in the link below.")
        
        fallback_es = translate_to_spanish(default_summary, max_chars=320)
        bullets_es.append(f"📌 **¿Qué sucedió?**: {fallback_es}")
        bullets_es.append("🔍 **Detalles clave**: Consulta el enlace original para leer la cobertura completa.")

    return {
        "title_en": title_en,
        "title_es": title_es,
        "bullets_en": bullets_en,
        "bullets_es": bullets_es,
        "url": url
    }
