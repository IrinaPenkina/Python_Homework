# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


# import math

# s = int(input('Задайте сумму чисел: '))
# n = int(input('Задайте произведение чисел: '))

# dis = s * s - 4 * n 
# sqrt_val = math.sqrt(abs(dis)) 

# if dis > 0:
#     x = round((-s + sqrt_val) /(-2))
#     y = round(s - x, 0)
#     print(f"Значения: {x}, {y}") 
    
# elif dis == 0:
#     x = round(s / 2, 0)
#     y = round(s - x, 0)
#     print(f"Значения: {x}, {y}")
 
# else: 
#     print('Значений нет')
 

x = int(input('Задайте сумму чисел: '))
y = int(input('Задайте произведение чисел: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i,j)

# ВАЖНО: Решение через дискриминант самое простое и оптимальное.