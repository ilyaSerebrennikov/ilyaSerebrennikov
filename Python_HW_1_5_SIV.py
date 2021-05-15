'''
Lesson_1_5
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки
(соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
'''
while True:
    user_revenue = input("Сколько? Укажите значение выручки в рублях! \n")
    if user_revenue.isdigit():
       user_revenue = int(user_revenue)
       break
    else:
        print("Введено Не число!!!")

while True:
    user_total_costs = input("Сколько расходов понесли? Расходы  указать в рублях! \n")
    if user_total_costs.isdigit():
        user_total_costs = int(user_total_costs)
        break
    else:
        print("Введено Не число!!!")

fin_result = user_revenue - user_total_costs

if fin_result >0:
    ratio =  round((fin_result/user_revenue),2)
    print(f'Прибыль по выручке составляет: {fin_result},\n Соотношение {ratio}!')
    while True:
        worker_number = input("Укажите сколько у вас сотрудников!\n")
        if worker_number.isdigit():
            worker_number = int(worker_number)
            ratio_per_worker = round((fin_result/worker_number),2)
            print(f'Показатель рентабельности по сотрудникам:Соотношение {ratio_per_worker}!')
            break
        else:
            print("Введено Не число!!!Количество сотрудников должно быть числом!!!")
else:
    print(f'Убыток по выручке составляет: {fin_result}!\n')
