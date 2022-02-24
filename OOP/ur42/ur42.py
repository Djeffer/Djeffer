# pip install beautifulsoup4 или pip install bs4
from bs4 import BeautifulSoup
import re

# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois')
#     if 'Copywriter' in whois:
#         return tag
#     return None


# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find('div', class_='name')  # find - возращает первый найденный элемент
# row = soup.find_all('div', class_='name')  # find - возращает все найденные элементы
# row = soup.find_all('div', class_='row')[1].find('div', class_='links')
# row = soup.find('div', {"class": 'name'})
# print(row)
# alena = soup.find('div', text='Alena').find_parent(class_='row')
# print(alena)
# row = soup.find('div', id='whois3').find_next_sibling()
# print(row)

# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('div', {'data-set': 'salary'})
# for i in row:
#     get_salary(i.text)

import requests
import csv

# r = requests.get('https://ru.wordpress.org/')
# print(r.status_code)
# print(r.headers)
# print(r.headers['Content-Type'])

# r = requests.get('https://ru.wordpress.org/')
# print(r.content)
# print(r.text)


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    res = re.sub(r'\D+', '', s)
    return res


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow((data['name'], data['url'], data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    s = soup.find_all('section', class_='plugin-section')[1]
    plugins = s.find_all('article')
    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        rating = plugin.find('span', class_='rating-count').find('a').text
        r = refined(rating)

        data = {'name': name, 'url': url, 'rating': r}
        write_csv(data)
    # return plugins


def main():
    url = 'https://ru.wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
