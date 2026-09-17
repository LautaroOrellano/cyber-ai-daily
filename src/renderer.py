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

def generate_edition_markdown(edition_number: int, dt: datetime, news: list) -> str:
    """Generates the markdown for a specific edition file."""
    human_date = format_date_human(dt)
    
    lead = news[0] if len(news) > 0 else None
    col1 = news[1] if len(news) > 1 else None
    col2 = news[2] if len(news) > 2 else None
    
    lines = [
        f"# 🗞️ The CyberAI Gazette — Edición N° {edition_number}",
        f"> **📅 Fecha:** {human_date}",
        "> **Resumen diario automatizado de Inteligencia Artificial & Ciberseguridad**",
        "",
        "---",
        ""
    ]
    
    if lead:
        cat_badge = CATEGORY_LABELS.get(lead["category"], "🌐 Tecnología")
        lines.extend([
            "## 📢 TITULAR PRINCIPAL DE PORTADA",
            "",
            f"### [{lead['title']}]({lead['link']})",
            f"> **Categoría:** {cat_badge} | **Fuente:** {lead['source']}",
            "",
            f"{lead['summary']}",
            "",
            f"👉 **[Leer artículo completo en {lead['source']} ↗]({lead['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.append("## 📰 OTRAS NOTICIAS DESTACADAS DE ESTA EDICIÓN\n")
    
    for item in [col1, col2]:
        if item:
            cat_badge = CATEGORY_LABELS.get(item["category"], "🌐 Tecnología")
            lines.extend([
                f"### 🔹 [{item['title']}]({item['link']})",
                f"> **Categoría:** {cat_badge} | **Fuente:** {item['source']}",
                "",
                f"{item['summary']}",
                "",
                f"🔗 **[Leer nota en {item['source']} ↗]({item['link']})**",
                "",
                "---",
                ""
            ])
            
    lines.extend([
        "## ℹ️ Acerca de esta publicación",
        "Este boletín ha sido generado de forma 100% autónoma mediante un pipeline de **GitHub Actions**.",
        "Monitorea diariamente los principales feeds y portales de ciberseguridad e inteligencia artificial.",
        "",
        "[⬅️ Volver a la portada principal](../../../README.md)"
    ])
    
    return "\n".join(lines)

def generate_readme_markdown(edition_number: int, dt: datetime, news: list, archive: list) -> str:
    """Generates the main README.md front page."""
    human_date = format_date_human(dt)
    date_iso = dt.strftime("%Y-%m-%d")
    
    lead = news[0] if len(news) > 0 else None
    col1 = news[1] if len(news) > 1 else None
    col2 = news[2] if len(news) > 2 else None
    
    lines = [
        "# 🗞️ THE CYBER-AI GAZETTE",
        "### *Crónicas Diarias de Inteligencia Artificial, Hackeos y Seguridad Digital*",
        "",
        f"> **📅 Edición de Hoy: N° {edition_number}** — *{human_date}*",
        "",
        "![Edición](https://img.shields.io/badge/Edici%C3%B3n-N%C2%B0_" + str(edition_number) + "-black?style=for-the-badge)",
        "![Noticias](https://img.shields.io/badge/Noticias-3_Diarias-blue?style=for-the-badge)",
        "![Pipeline](https://img.shields.io/badge/Pipeline-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)",
        "![Status](https://img.shields.io/badge/Estado-100%25_Aut%C3%B3nomo-success?style=for-the-badge)",
        "",
        "Bienvenido a **The CyberAI Gazette**, un periódico digital automatizado que se publica todos los días. Un pipeline en **GitHub Actions** rastrea la red, sintetiza las 3 novedades más impactantes sobre Inteligencia Artificial y Ciberseguridad, y emite una nueva tirada de noticias.",
        "",
        "---",
        ""
    ]
    
    if lead:
        cat_badge = CATEGORY_LABELS.get(lead["category"], "🌐 Tecnología")
        lines.extend([
            "## 📢 TITULAR PRINCIPAL (LEAD STORY)",
            "",
            f"### 📌 [{lead['title']}]({lead['link']})",
            f"> **Categoría:** {cat_badge} &nbsp;|&nbsp; **Fuente:** {lead['source']}",
            "",
            f"{lead['summary']}",
            "",
            f"👉 **[Leer artículo completo en {lead['source']} ↗]({lead['link']})**",
            "",
            "---",
            ""
        ])
        
    lines.append("## 📰 COLUMNAS DESTACADAS DEL DÍA\n")
    
    columns = [item for item in [col1, col2] if item]
    for idx, item in enumerate(columns, start=2):
        cat_badge = CATEGORY_LABELS.get(item["category"], "🌐 Tecnología")
        lines.extend([
            f"### 🔹 Columna {idx}: [{item['title']}]({item['link']})",
            f"> **Categoría:** {cat_badge} &nbsp;|&nbsp; **Fuente:** {item['source']}",
            "",
            f"{item['summary']}",
            "",
            f"🔗 **[Continuar leyendo en {item['source']} ↗]({item['link']})**",
            "",
            "---",
            ""
        ])
        
    # Hemeroteca / Archive table
    lines.extend([
        "## 🏛️ HEMEROTECA / EDICIONES ANTERIORES",
        "",
        "Puedes consultar las ediciones publicadas anteriormente en la siguiente tabla:",
        "",
        "| Edición | Fecha | Titular de Portada | Tópico |",
        "| :---: | :---: | :--- | :---: |"
    ])
    
    # Sort archive by edition descending, show up to last 15 in README
    sorted_archive = sorted(archive, key=lambda x: x["edition"], reverse=True)
    for entry in sorted_archive[:15]:
        ed_link = f"[{entry['edition']}]({entry['rel_path']})"
        cat_icon = "🛡️ Ciberseguridad" if entry.get("category") == "cyber" else "🤖 Inteligencia Artificial"
        # Truncate title in table if too long
        title = entry.get("title", "")
        if len(title) > 60:
            title = title[:57] + "..."
        lines.append(f"| #{ed_link} | {entry['date']} | [{title}]({entry.get('lead_link', '#')}) | {cat_icon} |")
        
    if len(sorted_archive) > 15:
        lines.append(f"\n*... y {len(sorted_archive) - 15} ediciones más en la carpeta `/editions`.*")
        
    # Footer / How it works
    lines.extend([
        "",
        "---",
        "",
        "## ⚙️ ¿Cómo funciona este repositorio?",
        "",
        "1. **Disparador Programado:** Cada día a las 11:00 UTC, un workflow de GitHub Actions (`.github/workflows/daily_edition.yml`) se despierta automáticamente.",
        "2. **Extracción y Curación:** Un script en Python consulta feeds RSS de fuentes líderes (*The Hacker News, Dark Reading, TechCrunch AI, MIT Tech Review*).",
        "3. **Selección Inteligente:** Selecciona las 3 noticias más recientes y de mayor impacto, alternando entre ciberseguridad y novedades en modelos/agentes de IA.",
        "4. **Publicación y Versionado:** Archiva la edición en `editions/` y actualiza esta portada (`README.md`), haciendo un `git commit` y `git push` autónomo.",
        "",
        "⭐ *Si te resulta útil para mantenerte al día, no dudes en dejarle una estrella al repositorio.*"
    ])
    
    return "\n".join(lines)
