import openai
import os
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime
import requests
import json

# === Environment Setup ===
load_dotenv()

# Newsapi.org API key from .env
news_api_key = os.environ.get("NEWS_API_KEY")

# === OpenAI API Client Configuration ===
client = openai.OpenAI()
model = "gpt-4o-mini"

def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}&pageSize=5"
    )
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent=4)
            news_json = json.loads(news)
            
            data = news_json
            
            # Access all the fiels == loop through
            status = data["status"]
            total_results = data["totalResults"]
            articles = data["articles"]
            final_news = []
            
            # Loop through articles
            for article in articles:
                source_name = article["source"]["name"]
                author = article["author"]
                title = article["title"]
                description = article["description"]
                url = article["url"]
                content = article["content"]
                title_description = f"""
                    Title: {title},
                    Author: {author},
                    Source: {source_name},
                    Description: {description},
                    URL: {url}
                """
                final_news.append(title_description)
                
            return final_news
    
        else:
            return []
                
        
    except requests.exceptions.RequestException as e:
        print("Error occured during API Request", e)
    

def main():
    news = get_news("bitcoin")
    print(news)

if __name__ == "__main__":
    main()