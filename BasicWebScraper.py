import requests
from bs4 import BeautifulSoup
url = input("Enter URL: ")
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
for link in soup.find_all("a"):
    print(link.get("href"))