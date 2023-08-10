import requests as rq
from bs4 import BeautifulSoup as bs
from functools import cache

@cache
def parser(num):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    url = f'https://baza-gai.com.ua/nomer/{num}'
    r = rq.get(url, headers=headers)
    html = bs(r.content, 'html.parser')

    return html


@cache
def creat_info(num):

    arr_year = parser(num).find_all('div', class_="plate-model-card__content-date-model")
    arr_model = parser(num).find_all('h4', class_='plate-model-card__content-title')
    arr_adition = parser(num).find_all('li', class_="list-group-item plate-model__list-item")

    year = arr_year[0].text

    model = arr_model[0].text.strip()
    model = model.splitlines()[0].strip() + ' ' + model.splitlines()[2].strip()

    registration = arr_adition[0].text.strip()
    registration = registration.splitlines()[1]

    sings = arr_adition[1].text.strip()
    sings = sings.splitlines()[1]

    adres = arr_adition[3].text.strip()
    adres = adres.splitlines()[2].strip()

    img = parser(num).find_all('img', class_="card-img plate-model-card__img")
    img = img[0]['src']
    img = f'https://baza-gai.com.ua{img}'

    # print(year)
    # print(model)
    # print(registration)
    # print(sings)
    # print(adres)
    # print(img)

    # def download(url):
    #     d_img = rq.get(url)
    #     o_img = open(model + '.png', 'wb')
    #     o_img.write(d_img.content)
    #     o_img.close()


    # download(img)

    car = [year, model, registration, sings, adres, img]

    return car