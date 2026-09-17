import os
import json
from datetime import datetime

CATEGORY_LABELS_EN = {
    "cyber": "🛡️ Cybersecurity & Breaches",
    "ai": "🤖 Artificial Intelligence & ML"
}

CATEGORY_LABELS_ES = {
    "cyber": "🛡️ Ciberseguridad & Brechas",
    "ai": "🤖 Inteligencia Artificial & ML"
}

def format_date_en(dt: datetime) -> str:
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return f"{days[dt.weekday()]}, {months[dt.month - 1]} {dt.day}, {dt.year}"

def format_date_es(dt: datetime) -> str:
    months = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return f"{days[dt.weekday()]}, {dt.day} de {months[dt.month - 1]} de {dt.year}"

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

def render_bullets(bullets: list) -> str:
    if bullets:
        return "\n\n".join(f"- {b}" for b in bullets)
    return "No summary available."

def generate_edition_markdown(edition_number: int, dt: datetime, news: list) -> str:
    """Generates the markdown for a specific edition file (English default + Spanish toggle)."""
    date_en = format_date_en(dt)
    
    lead = news[0] if len(news) > 0 else None
    secondary_stories = news[1:] if len(news) > 1 else []
    
    lines = [
        f"# 🗞️ The CyberAI Gazette — Issue #{edition_number}",
        f"> **📅 Date:** {date_en}",
        f"> **Automated Daily Digest ({len(news)} top stories in AI & Cybersecurity)**",
        "> *Bilingual Edition: English (default) & Spanish*",
        "",
        "---",
        ""
    ]
    
    if lead:
        cat_badge = CATEGORY_LABELS_EN.get(lead["category"], "🌐 Tech")
        lines.extend([
            "## 📢 LEAD STORY",
            "",
            f"### [{lead['title_en']}]({lead['link']})",
            f"> **Category:** {cat_badge} | **Source:** {lead['source']}",
            "",
            render_bullets(lead.get("bullets_en", [])),
            "",
            "<details>",
            "<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>",
            "<br>",
            f"> **Título en español:** *{lead.get('title_es', lead['title_en'])}*",
            "",
            render_bullets(lead.get("bullets_es", [])),
            "",
            "</details>",
            "",
            f"👉 **[Read full original story on {lead['source']} ↗]({lead['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.append(f"## 📰 TOP STORIES OF THIS ISSUE ({len(secondary_stories)} Stories)\n")
    
    for idx, item in enumerate(secondary_stories, start=2):
        cat_badge = CATEGORY_LABELS_EN.get(item["category"], "🌐 Tech")
        lines.extend([
            f"### 🔹 Story {idx}: [{item['title_en']}]({item['link']})",
            f"> **Category:** {cat_badge} | **Source:** {item['source']}",
            "",
            render_bullets(item.get("bullets_en", [])),
            "",
            "<details>",
            "<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>",
            "<br>",
            f"> **Título en español:** *{item.get('title_es', item['title_en'])}*",
            "",
            render_bullets(item.get("bullets_es", [])),
            "",
            "</details>",
            "",
            f"🔗 **[Read full original story on {item['source']} ↗]({item['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.extend([
        "## ℹ️ About this issue",
        "This edition was autonomously collected, purged of ads, and summarized using **GitHub Actions**.",
        "",
        "[⬅️ Back to Front Page](../../../README.md)"
    ])
    
    return "\n".join(lines)

def generate_readme_markdown(edition_number: int, dt: datetime, news: list, archive: list) -> str:
    """Generates the main README.md in English (Default), with inline Spanish collapsible toggle."""
    date_en = format_date_en(dt)
    
    lead = news[0] if len(news) > 0 else None
    secondary_stories = news[1:] if len(news) > 1 else []
    
    lines = [
        "# 🗞️ THE CYBER-AI GAZETTE",
        "### *Daily Chronicles of Artificial Intelligence, Hacks & Cybersecurity*",
        "",
        f"> **📅 Today's Edition: Issue #{edition_number}** — *{date_en}*",
        ">",
        "> 🌐 **Language:** **English (Default)** &nbsp;|&nbsp; [🇪🇸 Leer en Español (README.es.md)](README.es.md)",
        "",
        f"![Edition](https://img.shields.io/badge/Edition-Issue_%23{edition_number}-black?style=for-the-badge)",
        "![Language](https://img.shields.io/badge/Language-EN_%7C_ES-blue?style=for-the-badge)",
        f"![Stories](https://img.shields.io/badge/Stories-{len(news)}_Daily-2088FF?style=for-the-badge)",
        "![Pipeline](https://img.shields.io/badge/Pipeline-GitHub_Actions-success?style=for-the-badge&logo=githubactions&logoColor=white)",
        "![AdFree](https://img.shields.io/badge/Ads-0%25_Clean-success?style=for-the-badge)",
        "",
        "Welcome to **The CyberAI Gazette**, an automated daily newspaper. Every day, a **GitHub Actions** pipeline monitors 10 leading cybersecurity and artificial intelligence publications, strips ads and trackers, and compiles an executive digest in both **English** (default) and **Spanish**.",
        "",
        "---",
        ""
    ]
    
    if lead:
        cat_badge = CATEGORY_LABELS_EN.get(lead["category"], "🌐 Tech")
        lines.extend([
            "## 📢 LEAD STORY OF THE DAY",
            "",
            f"### 📌 [{lead['title_en']}]({lead['link']})",
            f"> **Category:** {cat_badge} &nbsp;|&nbsp; **Source:** {lead['source']}",
            "",
            render_bullets(lead.get("bullets_en", [])),
            "",
            "<details>",
            "<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>",
            "<br>",
            f"> **Título en español:** *{lead.get('title_es', lead['title_en'])}*",
            "",
            render_bullets(lead.get("bullets_es", [])),
            "",
            "</details>",
            "",
            f"👉 **[Read full article on {lead['source']} ↗]({lead['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.append(f"## 📰 TOP HIGHLIGHTS ({len(secondary_stories)} Stories)\n")
    
    for idx, item in enumerate(secondary_stories, start=2):
        cat_badge = CATEGORY_LABELS_EN.get(item["category"], "🌐 Tech")
        lines.extend([
            f"### 🔹 Column {idx}: [{item['title_en']}]({item['link']})",
            f"> **Category:** {cat_badge} &nbsp;|&nbsp; **Source:** {item['source']}",
            "",
            render_bullets(item.get("bullets_en", [])),
            "",
            "<details>",
            "<summary><b>🇪🇸 Ver resumen en español (Click to expand)</b></summary>",
            "<br>",
            f"> **Título en español:** *{item.get('title_es', item['title_en'])}*",
            "",
            render_bullets(item.get("bullets_es", [])),
            "",
            "</details>",
            "",
            f"🔗 **[Read full article on {item['source']} ↗]({item['link']})**",
            "",
            "---",
            ""
        ])
        
    # Archive table
    lines.extend([
        "## 🏛️ ARCHIVE / PREVIOUS ISSUES",
        "",
        "All previous editions are permanently preserved. Browse them here:",
        "",
        "| Issue | Date | Lead Headline | Topic |",
        "| :---: | :---: | :--- | :---: |"
    ])
    
    sorted_archive = sorted(archive, key=lambda x: x["edition"], reverse=True)
    for entry in sorted_archive[:15]:
        ed_link = f"[#{entry['edition']}]({entry['rel_path']})"
        cat_icon = "🛡️ Cybersecurity" if entry.get("category") == "cyber" else "🤖 Artificial Intelligence"
        title = entry.get("title_en") or entry.get("title", "")
        if len(title) > 65:
            title = title[:62] + "..."
        lines.append(f"| {ed_link} | {entry['date']} | [{title}]({entry.get('lead_link', '#')}) | {cat_icon} |")
        
    if len(sorted_archive) > 15:
        lines.append(f"\n*... and {len(sorted_archive) - 15} more archived editions in `/editions` directory.*")
        
    # How it works in English
    lines.extend([
        "",
        "---",
        "",
        "## ⚙️ How does this automated digest work?",
        "",
        "1. **Daily Trigger:** Every morning at 11:00 UTC, a GitHub Actions workflow (`.github/workflows/daily_edition.yml`) starts automatically.",
        "2. **Multi-Source Ingestion:** Scrapes and filters 10 leading global sources (*Dark Reading, The Hacker News, Krebs on Security, CyberScoop, SecurityWeek, Wired AI, TechCrunch AI, The Verge AI, MIT Tech Review, Hugging Face*).",
        "3. **Clean Extraction:** Pulls full body content, removing ads, trackers, cookie prompts, and sidebars.",
        "4. **Bilingual Synthesis:** Synthesizes structured bullets in **English** and **Spanish** (*What happened, Key details, Impact*).",
        "5. **Autonomous Commit & Push:** Archives the daily issue in `editions/` and updates this front page (`README.md`).",
        "",
        "⭐ *If you find this daily gazette helpful, don't forget to star the repository!*"
    ])
    
    return "\n".join(lines)

def generate_readme_es_markdown(edition_number: int, dt: datetime, news: list, archive: list) -> str:
    """Generates the Spanish version README.es.md."""
    date_es = format_date_es(dt)
    
    lead = news[0] if len(news) > 0 else None
    secondary_stories = news[1:] if len(news) > 1 else []
    
    lines = [
        "# 🗞️ THE CYBER-AI GAZETTE",
        "### *Crónicas Diarias de Inteligencia Artificial, Hackeos y Ciberseguridad*",
        "",
        f"> **📅 Edición de Hoy: N° {edition_number}** — *{date_es}*",
        ">",
        "> 🌐 **Idioma:** **Español** &nbsp;|&nbsp; [🇺🇸 Read in English (README.md)](README.md)",
        "",
        f"![Edición](https://img.shields.io/badge/Edici%C3%B3n-N%C2%B0_{edition_number}-black?style=for-the-badge)",
        "![Idioma](https://img.shields.io/badge/Idioma-Espa%C3%B1ol-yellow?style=for-the-badge)",
        f"![Noticias](https://img.shields.io/badge/Noticias-{len(news)}_Diarias-blue?style=for-the-badge)",
        "![Pipeline](https://img.shields.io/badge/Pipeline-GitHub_Actions-success?style=for-the-badge&logo=githubactions&logoColor=white)",
        "![AdFree](https://img.shields.io/badge/Publicidad-0%25_Limpio-success?style=for-the-badge)",
        "",
        "Bienvenido a **The CyberAI Gazette**, tu periódico digital automatizado. Cada día, un pipeline en **GitHub Actions** rastrea las 10 principales fuentes mundiales de ciberseguridad e inteligencia artificial, extrae los artículos completos sin publicidad ni banners molestos, y genera un resumen ejecutivo **en español** directamente en este repositorio.",
        "",
        "---",
        ""
    ]
    
    if lead:
        cat_badge = CATEGORY_LABELS_ES.get(lead["category"], "🌐 Tecnología")
        lines.extend([
            "## 📢 TITULAR PRINCIPAL (LEAD STORY)",
            "",
            f"### 📌 [{lead.get('title_es', lead['title_en'])}]({lead['link']})",
            f"> **Categoría:** {cat_badge} &nbsp;|&nbsp; **Fuente:** {lead['source']} &nbsp;|&nbsp; *Original:* `{lead['title_en']}`",
            "",
            render_bullets(lead.get("bullets_es", [])),
            "",
            f"👉 **[Ver nota original completa en {lead['source']} (inglés) ↗]({lead['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.append(f"## 📰 COLUMNAS DESTACADAS DEL DÍA ({len(secondary_stories)} Noticias)\n")
    
    for idx, item in enumerate(secondary_stories, start=2):
        cat_badge = CATEGORY_LABELS_ES.get(item["category"], "🌐 Tecnología")
        lines.extend([
            f"### 🔹 Columna {idx}: [{item.get('title_es', item['title_en'])}]({item['link']})",
            f"> **Categoría:** {cat_badge} &nbsp;|&nbsp; **Fuente:** {item['source']} &nbsp;|&nbsp; *Original:* `{item['title_en']}`",
            "",
            render_bullets(item.get("bullets_es", [])),
            "",
            f"🔗 **[Ver nota original completa en {item['source']} (inglés) ↗]({item['link']})**",
            "",
            "---",
            ""
        ])
        
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
        ed_link = f"[#{entry['edition']}]({entry['rel_path']})"
        cat_icon = "🛡️ Ciberseguridad" if entry.get("category") == "cyber" else "🤖 Inteligencia Artificial"
        title = entry.get("title_es") or entry.get("title_en") or entry.get("title", "")
        if len(title) > 60:
            title = title[:57] + "..."
        lines.append(f"| {ed_link} | {entry['date']} | [{title}]({entry.get('lead_link', '#')}) | {cat_icon} |")
        
    if len(sorted_archive) > 15:
        lines.append(f"\n*... y {len(sorted_archive) - 15} ediciones más en la carpeta `/editions`.*")
        
    lines.extend([
        "",
        "---",
        "",
        "## ⚙️ ¿Cómo funciona este periódico digital?",
        "",
        "1. **Disparador Diario:** Cada mañana a las 11:00 UTC, un workflow de GitHub Actions (`.github/workflows/daily_edition.yml`) se inicia automáticamente.",
        "2. **Monitoreo de 10 Fuentes Líderes:** Rastrear medios de referencia como *Dark Reading, The Hacker News, Krebs on Security, CyberScoop, SecurityWeek, Wired AI, TechCrunch AI, The Verge AI, MIT Tech Review y Hugging Face*.",
        "3. **Extracción Limpia:** Un script en Python ingresa a los sitios web originales y extrae el cuerpo puro del artículo, purgando anuncios, menús y pop-ups.",
        "4. **Traducción y Resumen en Español:** Procesa los puntos clave de las 5 noticias seleccionadas y los traduce al español en formato de viñetas claras (¿Qué pasó?, Detalles clave, Impacto).",
        "5. **Publicación Autónoma:** Genera la edición del día en `editions/` y actualiza esta portada (`README.md`), dejando un commit y push automático.",
        "",
        "⭐ *Si te resulta útil para mantenerte al día con IA y Ciberseguridad, déjale una estrella al repositorio.*"
    ])
    
    return "\n".join(lines)
