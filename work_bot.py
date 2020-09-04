import xlrd
import pandas as pd
import re

xls = pd.read_excel(r'https://github.com/Betonz/work_bot/blob/master/ListG.xlsx?raw=true', index_col=0)
xls2 = pd.read_excel(r'https://github.com/Betonz/work_bot/blob/master/ListG.xlsx?raw=true', index_col=0, sheet_name='Listtwo')
 
print (xls)
print (xls2)
 
def room(a=()):
    #a = int(a)
    if a in xls.index:
        print ('Площадь {} помещения:'.format(a), xls.at[a, 'Plosh'])
        print ('Высота потолков: ', xls.at[a, 'Plosh'])
        c = xls.at[a, 'Arenda']
        if c == True:
            print ('Договор аренды: ', xls.at[a, 'Dogovor'])
        else:
            print ('Арендаторы отсутствуют')
    else:
        print ('Нет такого помещения')
        
 
def floor(a=int()):
    x = int(a.replace(" этаж", ""))
    if x in xls2.index:
        print ('Площадь {} этажа: '.format(x), xls2.at[x,'Plosh2'])
        print ('Кабинетов на этаже: ', xls2.at[x,'Cabs'])
        print ('Занятых арендаторами площадей: ', xls2.at[x, 'Arenda S'])
        print ('Свободных площадей: ', xls2.at[x, 'Free S'])
    else:
        print ('Нет такого этажа')
        
 
def helpus():
    print ('Поиск по помещениям: введите номер в формате "А101-1" или "А101"')
    print ('Поиск по этажу: введите этаж в формате "1 этаж"')
    
    
# Добавить в цикл: если в а будет слово Этаж, запусти floor, и т.д. Б121-1
 
while True:    
    incom_value = input('Введите значение : ')
    floor_t = bool(re.search(r'^\d{1}\sэтаж', incom_value))
    help_t = bool(re.search(r'^\помощь', incom_value))      
    room_t = bool(re.search(r'^(А|Б|В|Г){1}\d{3}\W{1}\d{1}|^(А|Б|В|Г){1}\d{3}', incom_value))
    if floor_t == True:
        floor (incom_value)
    elif help_t == True:
        helpus()
    elif room_t == True:
        room (incom_value)
    else: 
        print ('Значение не верно')
