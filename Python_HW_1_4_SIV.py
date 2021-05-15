'''
Lesson_1_4
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
while True:
    user_number = input("Введите ЦЕЛОЕ число, а то будет 'НЕ колмильфо - 'NO comme il faut'! \n")
    if user_number.isdigit():
        user_number = int(user_number)
        max_digit = user_number % 10
        user_number = user_number // 10
        while user_number > 0:
            if user_number % 10 > max_digit:
                max_digit = user_number % 10
            user_number = user_number // 10
        print("Самая большая цифра в введённом Вами числе это " + str(max_digit) + "!")
        break
    else:
        if user_number.isalpha(): #предупреждающая надпись если пользователь ввёл текст
            print("'НЕ колмильфо - 'NO comme il faut'!Вы ввели текст, не число!")
        else:
            print('Вы ввели, ни текст, ни число!Введите число!')