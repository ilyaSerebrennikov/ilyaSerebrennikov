'''
3.Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найти в массиве медиану – элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Примечание: Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках.
'''
import random
#import cProfile - кто-то предложил эту библиотеку.На кой???

def median_search(list, frst, last):

    list = list.copy()
    ind = len(list) // 2

    if frst >= last:
        return list[ind]

    raw = list[ind]
    i = frst
    j = last

    while i <= j:

        while list[i] < raw:
            i += 1

        while list[j] > raw:
            j -= 1

        if i <= j:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1

    if ind < i:
        list[ind] = median_search(list, frst, j)

    elif j < ind:
        list[ind] = median_search(list, i, last)

    return list[ind]


def merge_sort(arr):

    def merge(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(list):

        if len(list) == 1:
            return list

        elif len(list) == 2:
            return list if list[0] <= list[1] else list[::-1]

        else:
            return merge(div_half(list[:len(list)//2]), div_half(list[len(list)//2:]))

    return div_half(arr)


MIN_ITEM = 0
MAX_ITEM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = random.randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]



print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', array, sep='\n')

median = median_search(array, 0, len(array) - 1)
print(f'Вот медиана: {median}')
# print(array, '\n')

print('А это отсортированный массив: ', merge_sort(array), sep='\n')
if median == merge_sort(array)[len(array)//2]:
    print('\n Сверка показала, что "Верно!"')
else:
    print('\nСверка показала, что "Ошибка!!!"')

