import csv
from bs4 import BeautifulSoup
import requests


def get_html(url):
    r = requests.get(url)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all('article', class_='plugin-card')
    for el in elements:
        try:
            name = el.find('')
        except ValueError:
            name = ''


def main():
    url = "https://ru.wordpress.org/plugins/browse/blocks/"
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()

