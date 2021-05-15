'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
#Здесь нужен цикл и выход из него или команда exit -
# исключения IOexeption проработать - это по-хорошему.
list_winter = ['декабрь', 'январь', 'февраль']
list_sprq = ['март', 'апрель', 'май']
list_summer = ['июнь', 'июль','август']
list_autumn = ['сентябрь', 'октябрь','ноябрь']
list_season =  ['Зима','Весна', 'Лето', 'Осень']
while True:
    usr_number = input("Введите число от 1 до 12 \n")
#times_of_year = {(12,1,2):'зима', (3,4,5) : 'весна', (6,7,8): 'лето', (9,10,11):'осень'}
#x = times_of_year
#print(x.get('зима'))
    if usr_number.isdigit():
        if int(usr_number) == 1:#что здесь делать?
            print(list_winter[1], list_season[0])
        elif int(usr_number) == 2:
            print(list_winter[2], list_season[0])
        elif int(usr_number) == 3:
            print(list_sprq[0], list_season[1])
        elif int(usr_number) == 4:
            print(list_sprq[1],list_season[1])
        elif int(usr_number) == 5:
            print(list_sprq[2],list_season[1])
        elif int(usr_number) == 6:
            print(list_summer[0],list_season[2])
        elif int(usr_number) == 7:
            print(list_summer[1],list_season[2])
        elif int(usr_number) == 8:
            print(list_summer[2],list_season[2])
        elif int(usr_number) == 9:
            print(list_autumn[0],list_season[3])
        elif int(usr_number) == 10:
            print(list_autumn[1],list_season[3])
        elif int(usr_number) == 11:
            print(list_autumn[2],list_season[3])
        elif int(usr_number) == 12:
            print(list_winter[0], list_season[0])
        break
    else:
        print('Вы ввели не числов.Введите число!')

'''
seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Choose a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
'''
