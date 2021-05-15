'''
1.Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
 заданный случайными числами на промежутке [-100; 100).
 Вывести на экран исходный и отсортированный массивы.
'''

import random

def bubble_sort(list):
    n = 1
    while n < len(list):
        count = 0
        for i in range(len(list) - 1 - (n - 1)):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                count += 1
        if count == 0:
            break
        n += 1

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
bubble_sort(array)
print('Он же, но после сортировки:', array, sep='\n')