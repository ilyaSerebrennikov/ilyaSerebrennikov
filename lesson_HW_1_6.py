'''
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 %
относительно предыдущего.
Требуется определить номер дня, на который общий
результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и
выводить одно натуральное число — номер дня.
'''

first_day = int(input("Введите результаты пробежки первого дня в км "))
target_res = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = first_day
while result_km < target_res:
        first_day = 1.1 * first_day
        result_days += 1
        result_km = result_km + first_day
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)

