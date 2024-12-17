import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
top100_page = response.text
soup = BeautifulSoup(top100_page, 'html.parser')
# print(soup.prettify())

movies = soup.find_all(name='h3', class_='title')

movie_list = []

for movie in movies:
    movie_names = movie.getText()
    movie_list.insert(0, movie_names)


for mov in movie_list:
    print(mov)
    with open('/Users/danny714/Desktop/Python/Day 45/100 movies to watch/movies.txt', 'a') as file:
        file.writelines(f'{mov} \n')
