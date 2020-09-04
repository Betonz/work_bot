import xlrd
import pandas as pd
import re
import telebot

bot = telebot.TeleBot('1228594799:AAEekqyZCwbJ3wGrVjeDa64RDHiWgzjZm50')

xls = pd.read_excel(r'https://github.com/Betonz/work_bot/blob/master/ListG.xlsx?raw=true', index_col=0)
xls2 = pd.read_excel(r'https://github.com/Betonz/work_bot/blob/master/ListG.xlsx?raw=true', index_col=0, sheet_name='Listtwo')
 
def room(a=()):    
    if a in xls.index:
        bot.send_message(message.from_user.id, 'Площадь {} помещения:'.format(a), xls.at[a, 'Plosh'])
        bot.send_message(message.from_user.id, 'Высота потолков: ', xls.at[a, 'Plosh'])
        c = xls.at[a, 'Arenda']
        if c == True:
            bot.send_message(message.from_user.id, 'Договор аренды: ', xls.at[a, 'Dogovor'])
        else:
            bot.send_message(message.from_user.id, 'Арендаторы отсутствуют')
    else:
        bot.send_message(message.from_user.id, 'Нет такого помещения')
        

def floor(a=int()):
    x = int(a.replace(" этаж", ""))
    if x in xls2.index:
        bot.send_message(message.from_user.id, 'Площадь {} этажа: '.format(x), xls2.at[x,'Plosh2'])
        bot.send_message(message.from_user.id, 'Кабинетов на этаже: ', xls2.at[x,'Cabs'])
        bot.send_message(message.from_user.id, 'Занятых арендаторами площадей: ', xls2.at[x, 'Arenda S'])
        bot.send_message(message.from_user.id, 'Свободных площадей: ', xls2.at[x, 'Free S'])
    else:
        bot.send_message(message.from_user.id, 'Нет такого этажа')
        
 
def helpus():
    bot.send_message(message.from_user.id, 'Поиск по помещениям: введите номер в формате "А101-1" или "А101"')
    bot.send_message(message.from_user.id, 'Поиск по этажу: введите этаж в формате "1 этаж"')
    
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    sti = str(message)
    floor_t = bool(re.search(r'^\d{1}\sэтаж', sti))
    help_t = bool(re.search(r'^\помощь', sti))      
    room_t = bool(re.search(r'^(А|Б|В|Г){1}\d{3}\W{1}\d{1}|^(А|Б|В|Г){1}\d{3}', sti))
    if floor_t == True:
        floor (sti)
    elif help_t == True:
        helpus ()
    elif room_t == True:
        room_t (sti)
    else:
        bot.send_message(message.from_user.id, 'Значение не верно')

bot.polling(none_stop=True, interval=0)

