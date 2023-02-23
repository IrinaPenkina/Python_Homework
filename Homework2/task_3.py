# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

n = int(input('Задайте ограничение: '))
result = []
pow = 1

while pow < n:
    pow *= 2
    if pow <= n:
        result.append(pow)

print(result)
