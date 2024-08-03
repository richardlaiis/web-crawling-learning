import requests
from bs4 import BeautifulSoup

r = requests.get("https://udn.com/news/story/6925/8126007")
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
# with open("test.txt", "w", encoding="utf8") as f:
#     f.write(soup)
tag = soup.p;
print(tag.text)