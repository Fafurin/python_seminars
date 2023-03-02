# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

numb = int(input("Введите целое число больше 1: "))

count = 1

sum = 0

while count <= numb:
    sum += round((1+1/numb)**numb, 3)
    count += 1

print(sum)

