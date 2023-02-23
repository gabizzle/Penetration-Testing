# Lab 1 - Recon Automation

# The code is to retrieve or scrape YouTube videos. BeautifulSoup is used as the library because it can parse and obtain data from websites, and it is open-sourced. 
# It begins by requesting the YouTube results. The code asks for a query and the next portion is where it gets the query you put in. 
# Example is asking for a video about Cats. It will then base the search by the query (which is Cats). 
# The results of the URLs with cats will then be stored. The URL will be ‘created’ or stored, and then it will return a video or list of videos and will be ‘printed’ out, which is the output of the code.

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
