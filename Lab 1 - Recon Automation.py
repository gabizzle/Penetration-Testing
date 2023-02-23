# Lab 1 - Recon Automation

import requests
from bs4 import BeautifulSoup

def search_videos(query):
    endpoint = f"https://www.youtube.com/results?search_query={query}" response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_urls = []
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        video_urls.append(f"https://www.youtube.com{vid['href']}")
    return video_urls

query = input("Enter your search query: ") 
video_urls = search_videos(query) 
print("YouTube Videos:")
for url in video_urls:
    print(url)