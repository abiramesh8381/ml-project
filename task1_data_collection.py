# task1_data_collection.py
# TrendPulse: Fetch Data from HackerNews API
# Marks: 20
# Author: <Your Name>
# This script fetches trending stories, assigns categories, and saves them as JSON.

import requests
import time
import datetime
import os
import json

# -------------------------------
# Step 1 — Get Top Story IDs
# -------------------------------
headers = {"User-Agent": "TrendPulse/1.0"}
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

try:
    story_ids = requests.get(top_url, headers=headers).json()
except Exception as e:
    print("Error fetching top stories:", e)
    story_ids = []

# Limit to first 500 IDs
story_ids = story_ids[:5]

# -------------------------------
# Step 2 — Fetch Story Details
# -------------------------------
categories = {
    "technology": ["AI","software","tech","code","computer","data","cloud","API","GPU","LLM"],
    "worldnews": ["war","government","country","president","election","climate","attack","global"],
    "sports": ["NFL","NBA","FIFA","sport","game","team","player","league","championship"],
    "science": ["research","study","space","physics","biology","discovery","NASA","genome"],
    "entertainment": ["movie","film","music","Netflix","game","book","show","award","streaming"]
}

stories = []
counts = {cat:0 for cat in categories}

for cat, keywords in categories.items():
    for sid in story_ids:
        if counts[cat] >= 25:  # limit 25 per category
            break
        try:
            url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
            story = requests.get(url, headers=headers).json()
            if not story or "title" not in story:
                continue

            title = story["title"].lower()
            if any(kw.lower() in title for kw in keywords):
                stories.append({
                    "post_id": story.get("id"),
                    "title": story.get("title").strip(),
                    "category": cat,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by"),
                    "collected_at": datetime.datetime.now().isoformat()
                })
                counts[cat] += 1
        except Exception as e:
            print(f"Error fetching story {sid}:", e)
            continue
    time.sleep(2)  # wait between categories

# -------------------------------
# Step 3 — Save to JSON
# -------------------------------
os.makedirs("data", exist_ok=True)
filename = f"data/trends_{datetime.datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(stories, f, indent=2)

print(f"Collected {len(stories)} stories. Saved to {filename}")
