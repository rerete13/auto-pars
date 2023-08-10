import json
import datetime



def get_count_days(id):

    id = str(id)

    with open('users.json', 'r') as file:
        data = json.load(file)

    now = datetime.datetime.now()
    now = str(now.strftime("%d-%m-%Y %H:%M:%S"))

    get_time = data[id]['info']['bot-start']

    now = datetime.datetime.strptime(now, '%d-%m-%Y %H:%M:%S')
    time_obj = datetime.datetime.strptime(get_time, '%d-%m-%Y %H:%M:%S')

    res = now - time_obj

    return res


def get_user_account_info(id):

    id = str(id)    

    with open('users.json', 'r') as file:
        data = json.load(file)


    data[id]['info']['findings-count'] = len(data[id]['findings'])


    with open(f'users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    language = data[id]['info']['language']
    try_to_win = data[id]['info']['try-to-win']
    findings_count = data[id]['info']['findings-count']

    subscribe_count = data[id]['subscribe']['count']
    subscribe_sub_date = data[id]['subscribe']['sub-date']
    subscribe_status = data[id]['subscribe']['status']




    arr_acount_info = [findings_count, language, try_to_win, subscribe_count, subscribe_sub_date, subscribe_status]

    return arr_acount_info









