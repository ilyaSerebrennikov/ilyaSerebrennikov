'''
4.Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове
'''

#word_new = input(str())

#print(, sep='\n')


my_str1 = input(str("введите строку "))
my_word = []
num = 1
while True:
    if my_str1.isalpha():
        for el in range(my_str1.count(' ') + 1):
            my_word = my_str1.split()
            if len(str(my_word)) <= 10:
                print(f" {num} {my_word[el]}")
                num += 1
            else:
                print(f" {num} {my_word[el][0:10]}")
                num += 1
        break
    else:
        print("Введенное Вами значение не является строковой переменной!")
        break

