'''
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369
'''

print("Приветствую! Введите число")
while True:
    usr_numb = input("Введите ЦЕЛОЕ число, а то будет Ерунда \n")
    if usr_numb.isdigit():
        usr_numb = int(usr_numb) #если число - установить тип целое
        nn_numb = int(str(usr_numb) * 2)
        nnn_numb = int(str(usr_numb) * 3)
        result = int(usr_numb) + int(nn_numb) + int(nnn_numb)
        print(str(usr_numb) + " + " + str(nn_numb) + " + " + str(nnn_numb) + " будет " + str(result) + "!")
        break
    else:
        if usr_numb.: #предупреждающая надпись если пользователь ввёл текст
            print("Ерунда))))!Вы ввели текст, не число!")
        else:
            print('Вы ввели, ни текст, ни число!')
