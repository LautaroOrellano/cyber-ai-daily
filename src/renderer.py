import os
import json
from datetime import datetime

CATEGORY_LABELS = {
    "cyber": "🛡️ Ciberseguridad & Brechas",
    "ai": "🤖 Inteligencia Artificial & ML"
}

def format_date_human(dt: datetime) -> str:
    months = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    day_name = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][dt.weekday()]
    return f"{day_name}, {dt.day} de {months[dt.month - 1]} de {dt.year}"

def load_archive_index(archive_path: str) -> list:
    if os.path.exists(archive_path):
        try:
            with open(archive_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_archive_index(archive_path: str, data: list):
    os.makedirs(os.path.dirname(archive_path), exist_ok=True)
    with open(archive_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def render_story_bullets(item: dict) -> str:
    bullets = item.get("bullets", [])
    if bullets:
        return "\n\n".join(f"- {b}" for b in bullets)
    return item.get("summary", "Sin resumen disponible.")

def generate_edition_markdown(edition_number: int, dt: datetime, news: list) -> str:
    """Generates the markdown for a specific edition file."""
    human_date = format_date_human(dt)
    
    lead = news[0] if len(news) > 0 else None
    col1 = news[1] if len(news) > 1 else None
    col2 = news[2] if len(news) > 2 else None
    
    lines = [
        f"# 🗞️ The CyberAI Gazette — Edición N° {edition_number}",
        f"> **📅 Fecha:** {human_date}",
        "> **Resumen diario automatizado de Inteligencia Artificial & Ciberseguridad (100% en Español)**",
        "",
        "---",
        ""
    ]
    
    if lead:
        cat_badge = CATEGORY_LABELS.get(lead["category"], "🌐 Tecnología")
        title_es = lead.get("title_es") or lead["title"]
        title_en = lead.get("title_en") or lead["title"]
        lines.extend([
            "## 📢 TITULAR PRINCIPAL DE PORTADA",
            "",
            f"### [{title_es}]({lead['link']})",
            f"> **Categoría:** {cat_badge} | **Fuente:** {lead['source']}",
            f"> *Título original:* `{title_en}`",
            "",
            render_story_bullets(lead),
            "",
            f"👉 **[Ver artículo original en {lead['source']} (inglés) ↗]({lead['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.append("## 📰 OTRAS NOTICIAS DESTACADAS DE ESTA EDICIÓN\n")
    
    for item in [col1, col2]:
        if item:
            cat_badge = CATEGORY_LABELS.get(item["category"], "🌐 Tecnología")
            title_es = item.get("title_es") or item["title"]
            title_en = item.get("title_en") or item["title"]
            lines.extend([
                f"### 🔹 [{title_es}]({item['link']})",
                f"> **Categoría:** {cat_badge} | **Fuente:** {item['source']}",
                f"> *Título original:* `{title_en}`",
                "",
                render_story_bullets(item),
                "",
                f"🔗 **[Ver artículo original en {item['source']} (inglés) ↗]({item['link']})**",
                "",
                "---",
                ""
            ])
            
    lines.extend([
        "## ℹ️ Acerca de esta publicación",
        "Este boletín ha sido generado y sintetizado de forma autónoma mediante un pipeline de **GitHub Actions**.",
        "Extrae el texto completo de las noticias, elimina la publicidad/rastreadores y traduce los puntos esenciales al español.",
        "",
        "[⬅️ Volver a la portada principal](../../../README.md)"
    ])
    
    return "\n".join(lines)

def generate_readme_markdown(edition_number: int, dt: datetime, news: list, archive: list) -> str:
    """Generates the main README.md front page."""
    human_date = format_date_human(dt)
    
    lead = news[0] if len(news) > 0 else None
    col1 = news[1] if len(news) > 1 else None
    col2 = news[2] if len(news) > 2 else None
    
    lines = [
        "# 🗞️ THE CYBER-AI GAZETTE",
        "### *Crónicas Diarias de Inteligencia Artificial, Hackeos y Ciberseguridad*",
        "",
        f"> **📅 Edición de Hoy: N° {edition_number}** — *{human_date}*",
        "",
        "![Edición](https://img.shields.io/badge/Edici%C3%B3n-N%C2%B0_" + str(edition_number) + "-black?style=for-the-badge)",
        "![Idioma](https://img.shields.io/badge/Idioma-Espa%C3%B1ol-yellow?style=for-the-badge)",
        "![Noticias](https://img.shields.io/badge/Noticias-3_Diarias-blue?style=for-the-badge)",
        "![Pipeline](https://img.shields.io/badge/Pipeline-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)",
        "![AdFree](https://img.shields.io/badge/Publicidad-0%25_Limpio-success?style=for-the-badge)",
        "",
        "Bienvenido a **The CyberAI Gazette**, tu periódico digital automatizado. Cada día, un pipeline en **GitHub Actions** rastrea las principales fuentes mundiales de ciberseguridad e inteligencia artificial, extrae los artículos completos sin publicidad ni banners molestos, y genera un resumen ejecutivo **en español** directamente en este repositorio.",
        "",
        "---",
        ""
    ]
    
    if lead:
        cat_badge = CATEGORY_LABELS.get(lead["category"], "🌐 Tecnología")
        title_es = lead.get("title_es") or lead["title"]
        title_en = lead.get("title_en") or lead["title"]
        lines.extend([
            "## 📢 TITULAR PRINCIPAL (LEAD STORY)",
            "",
            f"### 📌 [{title_es}]({lead['link']})",
            f"> **Categoría:** {cat_badge} &nbsp;|&nbsp; **Fuente:** {lead['source']} &nbsp;|&nbsp; *Original:* `{title_en}`",
            "",
            render_story_bullets(lead),
            "",
            f"👉 **[Ver nota original completa en {lead['source']} (inglés) ↗]({lead['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.append("## 📰 COLUMNAS DESTACADAS DEL DÍA\n")
    
    columns = [item for item in [col1, col2] if item]
    for idx, item in enumerate(columns, start=2):
        cat_badge = CATEGORY_LABELS.get(item["category"], "🌐 Tecnología")
        title_es = item.get("title_es") or item["title"]
        title_en = item.get("title_en") or item["title"]
        lines.extend([
            f"### 🔹 Columna {idx}: [{title_es}]({item['link']})",
            f"> **Categoría:** {cat_badge} &nbsp;|&nbsp; **Fuente:** {item['source']} &nbsp;|&nbsp; *Original:* `{title_en}`",
            "",
            render_story_bullets(item),
            "",
            f"🔗 **[Ver nota original completa en {item['source']} (inglés) ↗]({item['link']})**",
            "",
            "---",
            ""
        ])
        
    # Hemeroteca / Archive table
    lines.extend([
        "## 🏛️ HEMEROTECA / EDICIONES ANTERIORES",
        "",
        "Todas las ediciones anteriores quedan archivadas de forma permanente. Puedes consultarlas aquí:",
        "",
        "| Edición | Fecha | Titular de Portada (Español) | Tópico |",
        "| :---: | :---: | :--- | :---: |"
    ])
    
    sorted_archive = sorted(archive, key=lambda x: x["edition"], reverse=True)
    for entry in sorted_archive[:15]:
        ed_link = f"[{entry['edition']}]({entry['rel_path']})"
        cat_icon = "🛡️ Ciberseguridad" if entry.get("category") == "cyber" else "🤖 Inteligencia Artificial"
        title = entry.get("title_es") or entry.get("title", "")
        if len(title) > 60:
            title = title[:57] + "..."
        lines.append(f"| #{ed_link} | {entry['date']} | [{title}]({entry.get('lead_link', '#')}) | {cat_icon} |")
        
    if len(sorted_archive) > 15:
        lines.append(f"\n*... y {len(sorted_archive) - 15} ediciones más en la carpeta `/editions`.*")
        
    # How it works section
    lines.extend([
        "",
        "---",
        "",
        "## ⚙️ ¿Cómo funciona este periódico digital?",
        "",
        "1. **Disparador Diario:** Cada mañana a las 11:00 UTC, un workflow de GitHub Actions (`.github/workflows/daily_edition.yml`) se inicia automáticamente.",
        "2. **Extracción Anti-Publicidad:** Un script en Python ingresa a los sitios web originales y extrae el cuerpo puro del artículo, purgando anuncios, menús y pop-ups.",
        "3. **Traducción y Resumen en Español:** Procesa los puntos clave de cada noticia y los traduce al español en formato de viñetas claras (¿Qué pasó?, Detalles clave, Impacto).",
        "4. **Publicación Autónoma:** Genera la edición del día en `editions/` y actualiza esta portada (`README.md`), dejando un commit y push automático.",
        "",
        "⭐ *Si te resulta útil para mantenerte al día con IA y Ciberseguridad, déjale una estrella al repositorio.*"
    ])
    
    return "\n".join(lines)
