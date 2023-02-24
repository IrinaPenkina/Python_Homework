# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# from random import *
# n = int(input('Задайте количество монет: '))
# coins = []
# count1 = 0
# count2 = 0

# for i in range(n):
#     c = randint(0, 1)
#     if c == 0:
#         count1 += 1
#     else:
#         count2 += 1
#     coins.append(c)

# print(coins)

# if count1 < count2:
#     print(count1)
# else:
#     print(count2)

# import random

# n = int(input('Задайте количество монет: '))
# a = [random.randint(0,1) for _ in range (n)]
# print(a)
# if a.count(0) <= a.count(1):
#     print(a.count(0))
# else:
#     print(a.count(1))

# ВАЖНО: этот алгоритм работает дольше из-за применения метода count.
# Сложность вметода count возрастает нелинейно при увеличении массива.

from random import randint
coins = [randint(0, 1) for _ in range(int(input('Введите количество монет: ')))]
print(coins)
print(min(coins.count(0), coins.count(1)))
