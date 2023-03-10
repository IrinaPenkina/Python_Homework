# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def summa(a, b):
    if b == 0:
        return a
    return 1 + summa(a, b - 1)

n = int(input('Задайте первое неотрицательное число: '))
m = int(input('Задайте второе неотрицательное число: '))

if n < 0 or m < 0:
    print ('Оба числа должны быть неотрицательными. Сложение не будет выполнено.')
else:
    print(summa(n, m))

