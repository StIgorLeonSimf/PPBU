import requests
from bs4 import BeautifulSoup

""" https://www.hse.ru/staff/allat"""


def get_main(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('h1', class_='person-caption').text
    # print(name)
    pos = soup.find('span', class_='person-appointment-title').text[:-2]
    # print(pos)
    langs = soup.find('dt', class_='b').find_all('dd')
    res = (name, pos)
    print(res)
    for l in langs:
        print(l.text)


# get_main('https://www.hse.ru/staff/allat/')
# get_main('https://www.hse.ru/org/persons/135897')
# get_main('https://www.hse.ru/org/persons/63890353')
# pul_addres = (
#     'https://www.hse.ru/staff/allat/',
#     'https://www.hse.ru/org/persons/135897',
#     'https://www.hse.ru/org/persons/63890353'
# )
endpoints = ('135897', '63890353')
for point in endpoints:
    get_main(f'https://www.hse.ru/org/persons/{point}')
