import requests
from bs4 import BeautifulSoup
from web_searching import web_search
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List

def web_scrape(url: str) -> str:
    try:
        headers = {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/58.0.3029.110 Safari/537.3"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text(separator=" ", strip=True)
            return page_text

        else:
            return f"Failed to retrieve {url}. Status code: {response.status_code}"

    except Exception as e:
        print(f"Error occurred while scraping {url}: {e}")
        return ""