import json
from datetime import datetime

# Function to save news to a file
def save_news(news_list, filename='news.json'):
    with open(filename, 'w') as file:
        json.dump(news_list, file)

# Function to load news from a file
def load_news(filename='news.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to add a news item
def add_news_item(news_item, news_list):
    news_list.append(news_item)
    save_news(news_list)

# Function to filter news by date
def filter_news_by_date(news_list, date):
    return [news for news in news_list if news['date'] == date]

# Function to filter news by source
def filter_news_by_source(news_list, source):
    return [news for news in news_list if news['source'] == source]

# Function to get the latest news
def get_latest_news(news_list):
    return sorted(news_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)
