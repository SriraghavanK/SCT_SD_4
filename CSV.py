import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = []
for item in soup.find_all('article', class_='product_pod'):
    title = item.h3.a['title']
    price = item.find('p', class_='price_color').text
    rating = item.p['class'][1]
    books.append([title, price, rating])

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Rating'])
    writer.writerows(books)
