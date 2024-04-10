
import string
from bs4 import BeautifulSoup
import requests

# with open("./Day 45 - Beautiful Soup/website.html", encoding="utf-8") as file:
#     contents = file.read()

# #print(contents)

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)

# # print(soup.prettify())
# # print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)

# for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))
#     pass

# heading = soup.find(name="h1", id="name").getText()
# # print(heading)

# section_heading = soup.find(name="h3", class_="heading").getText()
# #print(section_heading)

# company_url = soup.select_one(selector="p a")
# #print(company_url)

# name = soup.select_one(selector="#name") #css selectors
# print(name)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    parts = text.split('(')
    title = parts[0].strip()

    link = article_tag.select_one(selector="a")
    url = link.get("href")

    article_texts.append(title)
    article_links.append(url)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

maior_numero = max(article_upvotes)
index = article_upvotes.index(maior_numero)
print("Index: ", index)
print("Maior número de curtidas: ", maior_numero)

print("Notícia com mais curtidas: ", article_texts[index])
print("Link dessa notícia:", article_links[index])


