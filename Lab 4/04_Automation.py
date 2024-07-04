import requests
import re

# Enter the URL of the website to scrape
url = "https://facebook.com"

# Send a GET request to the URL and get the HTML response
response = requests.get(url)
html = response.text

# Use regular expressions to extract email addresses from the HTML
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html)

# Print the extracted email addresses
print(emails)
