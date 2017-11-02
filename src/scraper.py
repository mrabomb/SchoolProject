import requests
from bs4 import BeautifulSoup

page = requests.get("https://exchange.gemini.com")

#if shit broke
if (not page.status_code == 200):
    print("shit broke")

soup = BeautifulSoup(page.content, 'html.parser')

list(soup.children)
