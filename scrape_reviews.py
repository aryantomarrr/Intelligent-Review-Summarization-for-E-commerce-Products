import requests
from bs4 import BeautifulSoup
import time
import random
from typing import List
from deep_translator import GoogleTranslator

MAX_PAGES = 25  # Increased from 5 to 25
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    # Add more User-Agents here
]

def get_amazon_reviews(url: str, max_pages: int = MAX_PAGES) -> List[str]:
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }
    
    reviews = []
    page = 1

    base_url = url.split("?")[0] + "?"

    while page <= max_pages:
        print(f"Scraping page {page}...")
        try:
            url = f"{base_url}pageNumber={page}&ie=UTF8&reviewerType=all_reviews"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            for review in soup.find_all("div", {"data-hook": "review"}):
                review_text = review.find("span", {"data-hook": "review-body"}).text.strip()
                reviews.append(review_text)

            page += 1
            time.sleep(2)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            for i in range(3):
                print(f"Retrying ({i+1}/3)...")
                time.sleep(2)
                try:
                    response = requests.get(url, headers=headers)
                    response.raise_for_status()
                    break
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching the URL (retry {i+1}): {e}")
            else:
                break

    return reviews

def translate_text(text: str, target: str = 'en') -> str:
    try:
        translated_text = GoogleTranslator(source='auto', target=target).translate(text)
        return translated_text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text






















































# import requests
# from bs4 import BeautifulSoup
# import time
# import random
# from typing import List
# from deep_translator import GoogleTranslator

# MAX_PAGES = 5
# USER_AGENTS = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#     # Add more User-Agents here
# ]

# def get_amazon_reviews(url: str, max_pages: int = MAX_PAGES) -> List[str]:
#     headers = {
#         "User-Agent": random.choice(USER_AGENTS),
#         "Accept-Language": "en-US,en;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
#     }
    
#     reviews = []
#     page = 1

#     base_url = url.split("?")[0] + "?"

#     while page <= max_pages:
#         print(f"Scraping page {page}...")
#         try:
#             url = f"{base_url}pageNumber={page}&ie=UTF8&reviewerType=all_reviews"
#             response = requests.get(url, headers=headers)
#             response.raise_for_status()
#             soup = BeautifulSoup(response.content, 'html.parser')

#             for review in soup.find_all("div", {"data-hook": "review"}):
#                 review_text = review.find("span", {"data-hook": "review-body"}).text.strip()
#                 reviews.append(review_text)

#             page += 1
#             time.sleep(2)

#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching the URL: {e}")
#             for i in range(3):
#                 print(f"Retrying ({i+1}/3)...")
#                 time.sleep(2)
#                 try:
#                     response = requests.get(url, headers=headers)
#                     response.raise_for_status()
#                     break
#                 except requests.exceptions.RequestException as e:
#                     print(f"Error fetching the URL (retry {i+1}): {e}")
#             else:
#                 break

#     return reviews

# def translate_text(text: str, target: str = 'en') -> str:
#     try:
#         translated_text = GoogleTranslator(source='auto', target=target).translate(text)
#         return translated_text
#     except Exception as e:
#         print(f"Error translating text: {e}")
#         return text
