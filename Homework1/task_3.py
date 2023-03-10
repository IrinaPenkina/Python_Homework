# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

while True:
    n = int(input('Введите шестизначный номер билета: '))
    if n // 100000 == 0 or n // 100000 > 9:
        print('Введено не шестизначное число. Задача не имеет решения.')
    else:
        break

sum1 = 0
for i in range (3):
    sum1 += n % 10
    n //= 10

# print(sum1)

sum2 = 0
for i in range (3):
    sum2 += n % 10
    n //= 10

# print(sum2)

if sum1 == sum2:
    print('Билет счастливый!')
else:
    print ('Увы, билет не счастливый.')
