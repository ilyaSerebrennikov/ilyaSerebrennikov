'''
Lesson 1_1
1. Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел
и строк и сохраните в переменные, выведите на экран.
'''


student_name = 'ilya'
ilya_age = 34
ilya_py_exp = 0
ilya_py_status = 'student'
print("Имя  " + str(student_name) + ", возраст " + str(int(ilya_age)) + " года ," +
      str(int(ilya_py_exp)) + " опыт в Python," + " статус в Python - " + str(ilya_py_status))
master_name = str(input("Введите своё имя, Мастер!\n"))
master_age = int(input("Сколько Вам лет, Мастер?\n"))
master_py_exp = int(input("Сколько лет опыта работы в Python?\n"))
if master_age <= master_py_exp:
    print("Одной жизни мало?!)))")
else:
    print("Вроде, нормальная разница между возрастом и опытом)")
master_py_status = master_py_exp - ilya_py_exp
if 0 < master_py_status <= 1:
    master_py_status = 'student'
elif 1 < master_py_status <= 3:
    master_py_status = 'junior-developer'
elif 3 < master_py_status <= 5:
    master_py_status = 'middle-developer'
else:
    master_py_status = 'senior-developer or team-leader'
print("Мастера зовут " + str(master_name) + "," + "возраст Мастера " + str(int(master_age))+ " лет, "
    + " опыт в Python  " + str(int(master_py_exp)) + " лет , " + "статус в Python " + str(master_py_status) + "!")
