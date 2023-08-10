import telebot
import tokens
import getinfo
import topauto
from telebot import types
import city as where
import comments
import json
from america import get_america as get_bidfax
import datetime
from photos import get_ukr_img, get_ukr_links_img
from func import cleaning, change_symbols, is_subscriber, json_update
from getuser import get_user_account_info, get_count_days

bot = telebot.TeleBot(tokens.Token)


print('started')


@bot.message_handler(commands=['start'])
def start_message(message):
    json_update(bot, message)

    if is_subscriber(bot, message.chat.id) == True:
        pass
    else:
        bot.send_message(message.chat.id, f"<b>Підпишися на канал:</b> @autopars3", parse_mode='HTML')
        return False


    main_btns = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    one_btn = types.KeyboardButton('Меню')
    main_btns.add(one_btn)


    bot.send_message(message.chat.id, f"<b>Введіть номер у такій формі:</b> AA7777AA", reply_markup=main_btns, parse_mode='HTML')


@bot.message_handler(commands=['info'])
def start_message(message):
    json_update(bot, message)
    bot.send_message(message.chat.id, f"<b>Bласник:</b> @rerete13\n\nНа їжу:\n4441111132314539 \n\n<b>USDT (TRC20)</b> \nTVSrox5rnjdK7Y2WL4dji3qyfb9yGb616f \n\n <b>BTC</b> \nbc1qsmy29mvt4gmfuex8xscalvnu5vfg6hjaf796ph", parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def creating(message):
    json_update(bot, message)

    number = message.text.upper()

    if is_subscriber(bot, message.chat.id) == True:
        pass
    else:
        btn = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Підписатися', url='https://t.me/autopars3')
        btn.add(btn1)

        bot.send_message(message.chat.id, f"<b>Підпишися на канал:</b> @autopars3", reply_markup=btn)
        return False

    if number == 'МЕНЮ':

        btns = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілів у 2023', callback_data='top10')
        btn3 = types.InlineKeyboardButton(text='🛠 Автосервіси', callback_data='4')
        btn4 = types.InlineKeyboardButton(text='🔬 INFO', callback_data='3')
        btn5 = types.InlineKeyboardButton(text='🍫 Власник', callback_data='owner')
        btn6 = types.InlineKeyboardButton(text='🗣 Відгуки', callback_data='respon')
        btn7 = types.InlineKeyboardButton(text='👤 Акаунт', callback_data='account')

        btns.add(btn1, btn3, btn6, btn4, btn5, btn7)


        bot.send_message(message.chat.id, "Меню", reply_markup=btns)
        return 0
    
    else:

        with open('users.json', 'r') as file:
            data = json.load(file)
        
        now = datetime.datetime.now()
        time_now = str(now.strftime("%d-%m-%Y %H:%M:%S"))

        form = time_now, message.text
        data[str(message.from_user.id)]['findings'].append(form)

        with open(f'users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)



        try:

            wait = bot.send_message(message.chat.id, '⏳ Це може зайняти деякий час..')

            changed_number = change_symbols(number)

            car_info = getinfo.creat_info(changed_number)

            btns = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text='американськi', callback_data=json.dumps({"c": "u", "n": f"{number}"}))
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(btn1, back)

            verify = cleaning(car_info[2])

            car_name = car_info[1].split()
            car_name = car_name[0]

            real_img_links = get_ukr_links_img(str(changed_number), verify, car_name)

            real_img = get_ukr_img(real_img_links)

            bot.delete_message(message.chat.id, wait.id)

            if len(real_img) > 0:
                for i in range(len(real_img)):
                    bot.send_photo(message.chat.id, real_img[i])
                
                
                bot.send_message(message.chat.id, f'{car_info[1]}\n{car_info[0]}\n{car_info[3]} {changed_number}\n{car_info[2]}\n{car_info[4]}')

            else:
                bot.send_photo(message.chat.id, car_info[5], f'{car_info[1]}\n{car_info[0]}\n{car_info[3]} {changed_number}\n{car_info[2]}\n{car_info[4]}')



        except IndexError:
            bot.send_message(message.chat.id, f'Машину з номерним знаком\n"<b>{changed_number}</b>" \nне зеайдено', parse_mode='HTML')

        if len(number) > 10:
            try:
                btns = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton(text='американськi', callback_data=json.dumps({"c": "u", "n": f"{number}"}))
                back = types.InlineKeyboardButton(text='Назад', callback_data='back')
                btns.add(btn1, back)
                bot.send_message(message.chat.id, f'Машину з вінкодом: \n"<b>{number}</b>"\n бажаєте шукати по американським базах?', reply_markup=btns, parse_mode='HTML')

            except:
                bot.send_message(message.chat.id, f'Машину з номерним знаком\n"<b>{number}</b>" \nне зеайдено', parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: True)
def checck_callback(call):

    city = topauto.all_citys
    city_link = topauto.all_citys_link

    try:

        if call.data == 'top10':

            btns = types.InlineKeyboardMarkup(row_width=1)
            btn2 = types.InlineKeyboardButton(text='Топ-50 найпопулярніших нових автомобілів у 2023', callback_data='top50')
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')

            btns.add(btn2, back)

            arr_top10 = ''
            for i in range(10):
                arr_top10 += topauto.all_cars_out[i] + '\n'

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=arr_top10, reply_markup=btns)


        if call.data == 'top50':

            arr_top50 = ''
            for i in range(50):
                arr_top50 += topauto.all_cars_out[i] + '\n'

            btns = types.InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(back)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=arr_top50, reply_markup=btns)

        if call.data == '3':

            btns = types.InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(back)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='<b>Доступні команди:</b>\n\n/info', reply_markup=btns, parse_mode='HTML')


        if call.data == '4':

            btns = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text=city[0], callback_data='kyiv')
            btn2 = types.InlineKeyboardButton(text=city[1], callback_data='kyiv-ob')
            btn3 = types.InlineKeyboardButton(text=city[2], callback_data='vinnycia')
            btn4 = types.InlineKeyboardButton(text=city[4], callback_data='dnipro')
            btn5 = types.InlineKeyboardButton(text=city[10], callback_data='frankivsk')
            btn6 = types.InlineKeyboardButton(text=city[13], callback_data='lviv')
            btn7 = types.InlineKeyboardButton(text=city[15], callback_data='odesa')
            btn8 = types.InlineKeyboardButton(text=city[16], callback_data='poltava')
            btn9 = types.InlineKeyboardButton(text=city[21], callback_data='harkiv')
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, back)


            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Виберіть місто', reply_markup=btns)


        if call.data == 'owner':

            btns = types.InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(back)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="<b>Bласник:</b> @rerete13\n\n<b>На їжу:</b>\n4441111132314539 \n\n<b>USDT (TRC20)</b> \nTVSrox5rnjdK7Y2WL4dji3qyfb9yGb616f \n\n<b>BTC</b> \nbc1qsmy29mvt4gmfuex8xscalvnu5vfg6hjaf796ph", reply_markup=btns, parse_mode='HTML')


        def bot_out_city(x):

            btns = types.InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(back)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"⏳ Це може зайняти деякий час...")

            out = f'{city[x]}\n\n'

            for i in range(len(where.getcity(city_link[x])[0])):
                out += f'{where.getcity(city_link[x])[0][i]}\n\n'


            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"{out}", reply_markup=btns)


        if call.data == 'kyiv':
            bot_out_city(0)

        if call.data == 'kyiv-ob':
            bot_out_city(1)

        if call.data == 'vinnycia':
            bot_out_city(2)

        if call.data == 'dnipro':
            bot_out_city(4)

        if call.data == 'frankivsk':
            bot_out_city(10)

        if call.data == 'lviv':
            bot_out_city(13)

        if call.data == 'odesa':
            bot_out_city(15)

        if call.data == 'poltava':
            bot_out_city(16)

        if call.data == 'harkiv':
            bot_out_city(21)

        if call.data == 'respon':

            btns = types.InlineKeyboardMarkup(row_width=1)
            btn2 = types.InlineKeyboardButton(text='Ще кілька відгуків', callback_data='morerespon')
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(btn2, back)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"⏳ Це може зайняти деякий час...")

            out = ''
            for i in range(3):
                out += comments.comment(i)[0] + '\n\n\n'

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=out, reply_markup=btns)
        
        if call.data == 'morerespon':

            btns = types.InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(back)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"⏳ Це може зайняти деякий час...")

            out = ''
            for i in range(10):
                out += comments.comment(i)[0] + '\n\n\n'

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=out, reply_markup=btns)

        
        if call.data == 'account':

            days = get_count_days(call.message.chat.id)
            user_info = get_user_account_info(call.message.chat.id)


            btns = types.InlineKeyboardMarkup(row_width=1)
            back = types.InlineKeyboardButton(text='Назад', callback_data='back')
            btns.add(back)

            bot.edit_message_text(chat_id=call.message.chat.id, 
                                  message_id=call.message.id, text=f'👤 Мій акаунт: {call.message.chat.id} \n\n📝 Мова: {user_info[1]} \n⏳ Вік облікового запису: {days}  \n🔗 Кількість запитів: {user_info[0]} \n\n🎰 Квитків: {user_info[2]} \n💸 Преміум запити: {user_info[3]} \n🔑 Залишок преміум підписки: {user_info[4]} \n📇 Статус: {user_info[5]} ', 
                                  reply_markup=btns)



        if call.data == 'back':

            btns = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілі в 2023', callback_data='top10')
            btn3 = types.InlineKeyboardButton(text='🛠 Автосервіси', callback_data='4')
            btn4 = types.InlineKeyboardButton(text='🔬 INFO', callback_data='3')
            btn5 = types.InlineKeyboardButton(text='🍫 Власник', callback_data='owner')
            btn6 = types.InlineKeyboardButton(text='🗣 Відгуки', callback_data='respon')
            btn7 = types.InlineKeyboardButton(text='👤 Акаунт', callback_data='account')


            btns.add(btn1, btn3, btn6, btn4, btn5, btn7)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Меню', reply_markup=btns)

        try:
            cal = json.loads(call.data)["c"]
            data = json.loads(call.data)["n"]
            if cal == 'u':
                try:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Машину з вінкодом: \n"{data}"\n шукаємо по американським базам даних \nце може зайняти від 30 секунд до 1 хвилини\n\nТакож підпишіться на групу з ґіфками @stick_ochky')
                    bidfax = get_bidfax(data)
                    try:
                        for i in range(0, 9):
                            bot.send_photo(chat_id=call.message.chat.id, photo=bidfax[0][i])

                    except:
                        pass
                    bot.send_message(
                        call.message.chat.id, 
                        text=f'\n<b>{bidfax[1]}</b>\n\n<b>Аукціон:</b>\n{bidfax[2]}\n<b>Номер лоту:</b>\n{bidfax[3]}\n<b>Дата продажу:</b>\n{bidfax[4]}\n<b>Рік випуску:</b>\n{bidfax[5]}\n<b>VIN:</b>\n{bidfax[6]}\n<b>Стан:</b>\n{bidfax[7]}\n<b>Двигун:</b>\n{bidfax[8]}\n<b>Документи:</b>\n{bidfax[10]}\n<b>Місце продажу:</b>\n{bidfax[11]}\n<b>Основне ушкодження:</b>\n{bidfax[12]}\n<b>Другорядне пошкодження:</b>\n{bidfax[13]}\n<b>Оціночна вартість:</b>\n{bidfax[14]}$\n<b>Ціна ремонту:</b>\n{bidfax[15]}$\n<b>Коробка передач:</b>\n{bidfax[16]}\n<b>Колір кузова:</b>\n{bidfax[17]}\n<b>Привід:</b>\n{bidfax[18]}\n<b>Паливо:</b>\n{bidfax[19]}\n<b>Ключі:</b>\n{bidfax[20]}\n<b>Примітка:</b>\n{bidfax[21]}',
                        parse_mode='HTML'
                        )

                except Exception as e:
                    print(e)
                    bot.send_message(call.message.chat.id, text=f'Машину  з вінкодом: \n"<b>{data}</b>"\n не знайдено', parse_mode='HTML')
        except:
            pass

    except Exception as e:
        print('avoid crash')
        print(e)
        btns = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        btns.add(back)
        bot.send_message(call.message.chat.id, text='Виникла якась помилка...', reply_markup=btns)
        

bot.polling()