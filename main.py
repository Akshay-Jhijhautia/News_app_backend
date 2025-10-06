import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
base_url = os.getenv("NEWS_API_URL")

news = input("What sort of news are you interested in today? ")

url = f"{base_url}?q={news}&from=2025-09-06&sortBy=publishedAt&apiKey={api_key}"

response = requests.get(url)
news_content = response.json()
news_articles = news_content.get("articles", [])

for index, article in enumerate(news_articles, start=1):
    print(f"{index}. {article['title']}")
    print(article["url"])
    print()
