import re
import requests as rq
from bs4 import BeautifulSoup as bs
import telebot
import json
import datetime

def cleaning(text):
    pattern = r"[0-9-.]+"
    res = ''.join(re.findall(pattern, text))
    return res


def change_symbols(num):
    num = num.upper()
    arr_change_settings = [('А', 'A'), ('В', 'B'), ('К', 'K'), ('Т', 'T'), ('О', 'O'), ('М', 'M'), ('С', 'C'), ('Е', 'E'), ('Х', 'X'), ('Р', 'P'), ('І', 'I'), ('Н', 'H')]
    for j in arr_change_settings:
        num = num.replace(j[0], j[1])

    return num

def is_subscriber(bot, chat_id):
    chat_member = bot.get_chat_member('@autopars3', chat_id)
    # print(chat_member.status)

    arr_members_types = ['creator', 'administrator', 'member']
    for i in arr_members_types:
        if i == str(chat_member.status):
            return True

    return False


def json_update(bot, message):

    with open('users.json', 'r') as file:
            data = json.load(file)


    if str(message.from_user.id) in data:
        pass
    else:

        id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username

        now = datetime.datetime.now()
        time_now = str(now.strftime("%d-%m-%Y %H:%M:%S"))

        form = {
                "id": id,
                "first-name": first_name,
                "last-name": last_name,
                "user-name": username,
                "member-type": bot.get_chat_member('@autopars3', message.chat.id).status,
                "info": {
                        "findings-count": 0,
                        "bot-start": time_now,
                        "language": "UKR",
                        "try-to-win": 1
                },
                "subscribe": {
                        "count": 0,
                        "sub-date": 0,
                        "status": False
                    },
                "findings": []
        }
        data[message.from_user.id] = form

        with open(f'users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


