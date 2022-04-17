import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

request = requests.get(url=URL)

soup = BeautifulSoup(request.text, features="html.parser")
titles = soup.find_all(name="h3", class_="title")
titles_text = [title.string for title in titles]
titles_text.reverse()
file_output = "\n".join(titles_text)
with open(file="films.txt", mode="w", encoding="utf-8") as file:
    file.write(file_output)
