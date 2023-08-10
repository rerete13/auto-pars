import requests as rq
from bs4 import BeautifulSoup as bs
from functools import cache


def parser():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    url = f'https://baza-gai.com.ua'
    r = rq.get(url, headers=headers)
    html = bs(r.content, 'html.parser')

    return html

# from 0 to 9
def comment(num):
    comments = parser().find_all('tr', class_='pt-3 pb-3')
    finall_comment = comments[num].text.strip()
    finall_comment = finall_comment.splitlines()
    out = f'Номер: {finall_comment[4].strip()}\nАвтор: {finall_comment[15].strip()}\nВідгук: \n{finall_comment[20].strip()}\n{finall_comment[23].strip()}'
    number = f'{finall_comment[4].strip()}'
    number = number.replace(' ', '')
    return out, number

