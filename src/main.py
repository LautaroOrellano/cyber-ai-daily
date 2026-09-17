import os
import sys

# Configure UTF-8 encoding for console output across all platforms
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from datetime import datetime, timezone
from fetcher import get_top_news
from article_extractor import extract_and_summarize
from renderer import (
    generate_edition_markdown,
    generate_readme_markdown,
    load_archive_index,
    save_archive_index
)

def run():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    editions_dir = os.path.join(base_dir, "editions")
    archive_json_path = os.path.join(editions_dir, "archive.json")
    readme_path = os.path.join(base_dir, "README.md")
    
    print("🚀 [The CyberAI Gazette] Iniciando pipeline de recopilación diaria...")
    
    archive = load_archive_index(archive_json_path)
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    year_str = now.strftime("%Y")
    month_str = now.strftime("%m")
    
    # Calculate edition number
    existing_entry = next((e for e in archive if e.get("date") == date_str), None)
    if existing_entry:
        edition_number = existing_entry["edition"]
        print(f"ℹ️ Actualizando edición existente N° {edition_number} correspondiente a hoy ({date_str})...")
    else:
        edition_number = len(archive) + 1
        print(f"✨ Creando nueva edición N° {edition_number} ({date_str})...")
        
    # Fetch news (5 daily stories)
    news = get_top_news(n=5)
    if not news:
        print("❌ No se pudieron obtener noticias hoy. Abortando sin modificar archivos.")
        sys.exit(0)
        
    print(f"✅ Se seleccionaron {len(news)} noticias destacadas. Iniciando extracción limpia y traducción...")
    for i, item in enumerate(news, 1):
        print(f"   [{i}/{len(news)}] Procesando: {item['title'][:60]}...")
        extracted = extract_and_summarize(item["link"], item["title"], item["summary"])
        item["title_es"] = extracted["title_es"]
        item["title_en"] = extracted["title_en"]
        item["bullets"] = extracted["bullets"]
        
    # Generate daily edition file
    target_edition_dir = os.path.join(editions_dir, year_str, month_str)
    os.makedirs(target_edition_dir, exist_ok=True)
    edition_filename = f"{date_str}.md"
    edition_file_path = os.path.join(target_edition_dir, edition_filename)
    
    edition_content = generate_edition_markdown(edition_number, now, news)
    with open(edition_file_path, "w", encoding="utf-8") as f:
        f.write(edition_content)
    print(f"📄 Archivo de edición guardado en: {edition_file_path}")
    
    # Relative path from project root for markdown links
    rel_path = f"editions/{year_str}/{month_str}/{edition_filename}"
    lead_story = news[0]
    
    archive_entry = {
        "edition": edition_number,
        "date": date_str,
        "rel_path": rel_path,
        "title": lead_story["title"],
        "title_es": lead_story.get("title_es", lead_story["title"]),
        "category": lead_story["category"],
        "source": lead_story["source"],
        "lead_link": lead_story["link"]
    }
    
    # Update or append in archive
    if existing_entry:
        existing_index = archive.index(existing_entry)
        archive[existing_index] = archive_entry
    else:
        archive.append(archive_entry)
        
    save_archive_index(archive_json_path, archive)
    print("💾 Hemeroteca / archive.json actualizado.")
    
    # Generate README
    readme_content = generate_readme_markdown(edition_number, now, news, archive)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"📰 Portada README.md actualizada con la Edición N° {edition_number}.")
    print("🎉 Pipeline completado con éxito.")

if __name__ == "__main__":
    run()
