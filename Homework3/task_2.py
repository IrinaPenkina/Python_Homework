# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

lst = [randint(-10, 10) for _ in range(int(input('Задайте количество элементов массива: ')))]
print(f"Массив: {lst}")

# k = int(input('Задайте целое число: '))

# difference =  abs(lst[0] - k)
# target = lst[0]

# for i in range(1, len(lst)):
#     diff = abs(lst[i] - k)
#     if diff < difference:
#         difference = diff
#         target = lst[i]

# print(f"Самый близкий элемент массива к числу {k} -> {target}.")


x = int(input('x = '))

dct = {abs(x - item): item for item in lst}

print(dct)
print(dct[min(dct)])
