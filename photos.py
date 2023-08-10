import requests as rq
from bs4 import BeautifulSoup as bs
from func import cleaning
from pprint import pprint

def parser(num):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    url = f'https://platesmania.com/ua/gallery.php?fastsearch={num}'
    r = rq.get(url, headers=headers)
    html = bs(r.content, 'html.parser')

    return html

def parser_second(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = rq.get(url, headers=headers)
    html = bs(r.content, 'html.parser')

    return html


def check_name(link):
    panel = parser_second(link).find_all('h3', class_='text-center margin-bottom-10')

    panel = panel[0].find_all('a')
    panel = panel[0].text.split()
    panel = panel[0].upper()

    return panel


def get_ukr_links_img(num, date, name):
    panels = parser(f'{num}').find_all('div', class_='panel-body')

    verify = f'{date}'

    name = name.upper()

    arr_panel_links = []
    for i in range(len(panels)):
        link = panels[i].find_all('a')[0]['href']
        arr_panel_links.append(link)

    arr_panels_filter_img = []
    for i in arr_panel_links:

        link = f'https://platesmania.com{i}'
        panel = parser_second(link).find_all('ul', class_='list-unstyled')

        try:
            date = panel[1]

        except:
            continue


        date = date.find_all('li')[0]
        date = cleaning(str(date)).replace('-', ' ').split()
        date = f'{date[2]}.{date[1]}.{date[0]}'

        if date == verify and name == check_name(link):
            # print('find')
            arr_panels_filter_img.append(link)

    return arr_panels_filter_img



def get_opinion_about_num(links):

    for i in links:

        url = parser_second(i).find_all('div', class_='media media-v2')
        for j in url:

                url_sort = j.find_all('div')

                user_nick = url_sort[0].find_all('span')
                user_nick = user_nick[0].text

                date = url_sort[0].find_all('small')
                date = date[0].text

                arr_text = url_sort[0].find_all('p')
                text = arr_text[0].text

                text_photo = arr_text[0].find_all('a')
                text_photo = text_photo[0]['href']

                try:
                    print(user_nick)
                except:
                    print('nick')

                try:
                    print(date)
                except:
                    print('date')

                try:
                    print(text)
                except:
                    print('text')

                try:
                    print(text_photo)
                except:
                    print('no photo')

                




    

def get_ukr_img(links):

    arr_ukr_img = []
    for i in links:

        img = parser_second(i).find_all('img', class_='img-responsive center-block')
        arr_ukr_img.append(img[0]['src'])

    # print(arr_ukr_img)

    return arr_ukr_img



# x = get_ukr_links_img('AA1111AA', '09.11.2019', 'MERCEDES-BENZ')



# get_opinion_about_num(x)


# check_name('https://platesmania.com/ua/nomer15300636')






