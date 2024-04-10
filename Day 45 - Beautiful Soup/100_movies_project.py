import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_content = response.text

soup = BeautifulSoup(empire_content, "html.parser")

movies_list = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

formatted_list = [movie.getText() for movie in movies_list]

with open("./Day 45 - Beautiful Soup/movies.txt", "w", encoding="utf-8") as file:

    for movie in formatted_list.__reversed__():
        file.write(f"{movie}\n")