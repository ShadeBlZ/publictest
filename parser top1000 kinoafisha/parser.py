import requests
from bs4 import BeautifulSoup

import pandas as pd


def collect_rating():

    data = []

    for page_num in range(10):
        url = f'https://www.kinoafisha.info/rating/movies/?page={page_num}'
        response = requests.get(url)
        print(response)
        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content, 'lxml')

        entries = soup.find_all('div', class_='movieList_item movieItem movieItem-rating movieItem-position')
        print(len(entries))

        if len(entries) == 0:
            break

        for entry in entries:
            film_name = entry.find('a', class_='movieItem_title').text
            release_info = entry.find('span', class_='movieItem_year').text.split(', ')
            release_date, release_country = release_info
            rating = entry.find('span', class_='movieItem_itemRating miniRating miniRating-good').text
            genre = entry.find('span', class_='movieItem_genres').text


            data.append({'film_name': film_name, 'release_date': release_date, 'genre': genre, 'release_country': release_country, 'rating': rating})


    return data

top1000 = collect_rating()
df = pd.DataFrame(top1000)

df.to_excel('top1000.xlsx')
print('Сбор информации успешно завершен. Создан файл top1000.xlsx')
