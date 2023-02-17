# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

numb = int(input("Введите целое число больше 0: "))

count = 1

result = 1

if numb > 0:
    while count <= numb:
        result *= count
        count += 1
        print(result)








