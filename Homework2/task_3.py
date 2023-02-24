# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# n = int(input('Задайте ограничение: '))
# result = []
# pow = 1

# while pow < n:
#     pow *= 2
#     if pow <= n:
#         result.append(pow)

# print(result)


# n = int(input('Задайте ограничение: '))
# list = [2**i for i in range (1, n) if 2**i <= n] # тернарный оператор при задании списка
# print(list)

# НЕДОСТАТОК: дважды считается степень двойки


n = int(input('Задайте ограничение: '))
i = 0

while (pow := 2**i) <= n:
    print(pow, end=' ')
    i += 1
