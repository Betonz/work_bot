import pandas as pd
import re
import telebot
from telebot import types

bot = telebot.TeleBot('1228594799:AAEekqyZCwbJ3wGrVjeDa64RDHiWgzjZm50')

xls = pd.read_excel(r'https://github.com/Betonz/work_bot/blob/master/ListG.xlsx?raw=true', index_col=0)
xls2 = pd.read_excel(r'https://github.com/Betonz/work_bot/blob/master/ListG.xlsx?raw=true', index_col=0, sheet_name='Listtwo')
 
def room(message):
    if message.text in xls.index:
        bot.send_message(message.from_user.id, f'Площадь {message.text} помещения: {xls.at[message.text, "Plosh"]}')
        bot.send_message(message.from_user.id, f'Высота потолков: {xls.at[message.text, "Plosh"]}')
        c = xls.at[message.text, 'Arenda']
        if c == True:
            bot.send_message(message.from_user.id, f'Договор аренды: {xls.at[message.text, "Dogovor"]}')
        else:
            bot.send_message(message.from_user.id, 'Арендаторы отсутствуют')
    else:
        bot.send_message(message.from_user.id, 'Нет такого помещения')
        

def floor(message):
    x = int(message.text.replace(" этаж", ""))
    if x in xls2.index:
        bot.send_message(message.from_user.id, f'Площадь {x} этажа: {xls2.at[x,"Plosh2"]}')
        bot.send_message(message.from_user.id, f'Кабинетов на этаже: {xls2.at[x,"Cabs"]}')
        bot.send_message(message.from_user.id, f'Занятых арендаторами площадей: {xls2.at[x, "Arenda S"]}')
        bot.send_message(message.from_user.id, f'Свободных площадей: {xls2.at[x, "Free S"]}')
    else:
        bot.send_message(message.from_user.id, 'Нет такого этажа')
        
 
def helpus(message):
    bot.send_message(message.from_user.id, 'Поиск по помещениям: введите номер в формате "А101-1" или "А101"')
    bot.send_message(message.from_user.id, 'Поиск по этажу: введите этаж в формате "1 этаж"')

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('/Этаж')
    itembtn2 = types.KeyboardButton('/Комната')
    itembtn3 = types.KeyboardButton('/start')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.from_user.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(commands=['Этаж'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn = []
    for i in xls2.index.tolist():
        itembtn.append(types.KeyboardButton(f'{i} этаж'))
    itembtn.append(types.KeyboardButton('/start'))
    markup.add(*itembtn)
    bot.send_message(message.from_user.id, "Выберите этаж:", reply_markup=markup)

@bot.message_handler(commands=['Комната'])
def handle_start_help(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn = []
    for i in xls.index.tolist():
        itembtn.append(types.KeyboardButton(f'{i}'))
    itembtn.append(types.KeyboardButton('/start'))
    markup.add(*itembtn)
    bot.send_message(message.from_user.id, "Выберите комнату:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    sti = str(message.text)
    floor_t = bool(re.search(r'^\d{1}\sэтаж', sti))
    help_t = bool(re.search(r'^\помощь', sti))
    room_t = bool(re.search(r'^(А|Б|В|Г){1}\d{3}\W{1}\d{1}|^(А|Б|В|Г){1}\d{3}', sti))
    if floor_t == True:
        floor(message)
    elif help_t == True:
        helpus(message)
    elif room_t == True:
        room(message)
    else:
        bot.send_message(message.from_user.id, 'Значение не верно')

bot.polling(none_stop=True, interval=0)

