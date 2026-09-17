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
    ],
    "ai": [
        {"name": "TechCrunch AI", "url": "https://techcrunch.com/category/artificial-intelligence/feed/"},
        {"name": "The Verge AI", "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"},
        {"name": "MIT Technology Review", "url": "https://www.technologyreview.com/topic/artificial-intelligence/feed/"},
    ]
}

def clean_html_summary(html_text: str, max_chars: int = 280) -> str:
    """Cleans HTML tags and entities, returning a concise plain text summary."""
    if not html_text:
        return "Sin descripción disponible."
    
    soup = BeautifulSoup(html_text, "html.parser")
    # Remove script and style elements
    for script in soup(["script", "style", "figure", "img"]):
        script.decompose()
        
    text = soup.get_text(separator=" ")
    text = re.sub(r"\s+", " ", text).strip()
    
    if len(text) > max_chars:
        # Cut at last complete word
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
        for entry in feed.entries[:8]: # Check top recent entries
            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            
            # Summary can come in 'summary', 'description', or 'content'
            raw_summary = entry.get("summary") or entry.get("description") or ""
            if isinstance(raw_summary, list) and len(raw_summary) > 0:
                raw_summary = raw_summary[0].get("value", "")
                
            summary = clean_html_summary(raw_summary)
            
            # Publication timestamp
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

def get_top_3_news() -> list:
    """
    Fetches news from all sources and picks the 3 most relevant:
    1. Top story in Cybersecurity & Hacks
    2. Top story in Artificial Intelligence
    3. The freshest additional highlight (Wildcard / Feature)
    """
    cyber_items = []
    for src in SOURCES["cyber"]:
        cyber_items.extend(fetch_feed_items("cyber", src))
        
    ai_items = []
    for src in SOURCES["ai"]:
        ai_items.extend(fetch_feed_items("ai", src))
        
    # Sort both lists by timestamp descending
    cyber_items.sort(key=lambda x: x["timestamp"], reverse=True)
    ai_items.sort(key=lambda x: x["timestamp"], reverse=True)
    
    selected = []
    seen_links = set()
    
    # 1. Pick Top Cyber
    if cyber_items:
        top_cyber = cyber_items.pop(0)
        selected.append(top_cyber)
        seen_links.add(top_cyber["link"])
        
    # 2. Pick Top AI
    if ai_items:
        top_ai = ai_items.pop(0)
        selected.append(top_ai)
        seen_links.add(top_ai["link"])
        
    # 3. Pick 3rd story from remaining items
    remaining = [item for item in (cyber_items + ai_items) if item["link"] not in seen_links]
    remaining.sort(key=lambda x: x["timestamp"], reverse=True)
    
    if remaining:
        selected.append(remaining[0])
        
    return selected
