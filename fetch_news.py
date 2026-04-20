import requests
import json

def fetch_news():
    # Mock fetching news. Replace with actual API or feed.
    news_items = [
        {"title": f"Tech News Item {i+1}", "link": f"http://example.com/news{i+1}"}
        for i in range(10)
    ]
    with open('news.json', 'w') as f:
        json.dump(news_items, f)

if __name__ == "__main__":
    fetch_news()