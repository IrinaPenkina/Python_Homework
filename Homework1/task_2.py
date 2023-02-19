# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что 
# Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

while True:
    s = int(input('Задайте количество журавликов: '))
    if s % 6 != 0:
        print('Задача не имеет решения. Количество журавликов должно делиться на 6.')
    else:
        break
     
a = s // 6
b = 4 * a

print("Петя сделал {} журавликов, Сережа сделал {} журавликов, Катя сделала {} журавликов.". format(a, a, b))

