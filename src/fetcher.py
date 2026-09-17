import time
import re
import requests
import feedparser
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

SOURCES = {
    "cyber": [
        {"name": "The Hacker News", "url": "https://feeds.feedburner.com/TheHackersNews"},
        {"name": "Dark Reading", "url": "https://www.darkreading.com/rss.xml"},
        {"name": "SecurityWeek", "url": "https://www.securityweek.com/feed/"},
        {"name": "Krebs on Security", "url": "https://krebsonsecurity.com/feed/"},
        {"name": "CyberScoop", "url": "https://cyberscoop.com/feed/"},
    ],
    "ai": [
        {"name": "TechCrunch AI", "url": "https://techcrunch.com/category/artificial-intelligence/feed/"},
        {"name": "The Verge AI", "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"},
        {"name": "MIT Technology Review", "url": "https://www.technologyreview.com/topic/artificial-intelligence/feed/"},
        {"name": "Wired AI", "url": "https://www.wired.com/feed/tag/ai/latest/rss"},
        {"name": "Hugging Face Blog", "url": "https://huggingface.co/blog/feed.xml"},
    ]
}

def clean_html_summary(html_text: str, max_chars: int = 280) -> str:
    """Cleans HTML tags and entities, returning a concise plain text summary."""
    if not html_text:
        return "Sin descripción disponible."
    
    soup = BeautifulSoup(html_text, "html.parser")
    for script in soup(["script", "style", "figure", "img"]):
        script.decompose()
        
    text = soup.get_text(separator=" ")
    text = re.sub(r"\s+", " ", text).strip()
    
    if len(text) > max_chars:
        truncated = text[:max_chars]
        last_space = truncated.rfind(" ")
        if last_space != -1:
            truncated = truncated[:last_space]
        return truncated + "..."
    return text

def fetch_feed_items(category: str, source_info: dict) -> list:
    """Fetches and parses a single RSS feed."""
    items = []
    try:
        resp = requests.get(source_info["url"], headers=HEADERS, timeout=12)
        if resp.status_code != 200:
            print(f"⚠️ [{source_info['name']}] Status code: {resp.status_code}")
            return items
            
        feed = feedparser.parse(resp.content)
        for entry in feed.entries[:8]:
            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            
            raw_summary = entry.get("summary") or entry.get("description") or ""
            if isinstance(raw_summary, list) and len(raw_summary) > 0:
                raw_summary = raw_summary[0].get("value", "")
                
            summary = clean_html_summary(raw_summary)
            
            published_ts = time.time()
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                try:
                    published_ts = time.mktime(entry.published_parsed)
                except Exception:
                    published_ts = time.time()
                    
            if title and link:
                items.append({
                    "title": title,
                    "link": link,
                    "summary": summary,
                    "source": source_info["name"],
                    "category": category,
                    "timestamp": published_ts
                })
    except Exception as e:
        print(f"❌ Error fetching {source_info['name']}: {e}")
        
    return items

def get_top_news(n: int = 5) -> list:
    """
    Fetches news from all sources and balances between Cyber & AI:
    - 2 top stories in Cybersecurity & Hacks
    - 2 top stories in Artificial Intelligence & ML
    - 1 freshest additional story across both fields
    Total: 5 curated stories
    """
    cyber_items = []
    for src in SOURCES["cyber"]:
        cyber_items.extend(fetch_feed_items("cyber", src))
        
    ai_items = []
    for src in SOURCES["ai"]:
        ai_items.extend(fetch_feed_items("ai", src))
        
    cyber_items.sort(key=lambda x: x["timestamp"], reverse=True)
    ai_items.sort(key=lambda x: x["timestamp"], reverse=True)
    
    selected = []
    seen_links = set()
    
    def pick_from(item_list):
        for it in item_list:
            if it["link"] not in seen_links:
                seen_links.add(it["link"])
                selected.append(it)
                return True
        return False
        
    # Select 2 Cyber and 2 AI
    pick_from(cyber_items)
    pick_from(ai_items)
    pick_from(cyber_items)
    pick_from(ai_items)
    
    # Fill remaining up to n (5) from freshest overall
    remaining = [item for item in (cyber_items + ai_items) if item["link"] not in seen_links]
    remaining.sort(key=lambda x: x["timestamp"], reverse=True)
    
    for item in remaining:
        if len(selected) >= n:
            break
        selected.append(item)
        seen_links.add(item["link"])
        
    return selected
