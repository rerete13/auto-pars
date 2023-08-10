import topauto
import requests as rq
from bs4 import BeautifulSoup as bs
from functools import cache

link = topauto.all_citys_link

@cache
def parser(num):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    url = f'{num}'
    r = rq.get(url, headers=headers)
    html = bs(r.content, 'html.parser')

    return html

@cache
def getcity(name):

    city = parser(name).find_all('tr')
    links = parser(name).find_all('a', target="_blank")

    arr_about_places = []
    maps = []

    for i in range(1, len(city)):
        
        x = city[i].text.splitlines()
        out = f'{x[4].strip()}\n{x[9].strip()}\n{x[10][0:15]}'
        arr_about_places.append(out)
    
    # let = 'href'
    # for i in range(len(links)):
    #     x = f'{links[i][let]}'
    #     x.replace(' ', '-')
    #     maps.append(x)



    return arr_about_places, maps
    
