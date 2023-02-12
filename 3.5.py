# 4. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите длину ряда Фибоначчи: '))
numb1 = numb2 = numb3 = 1
numb4 = 0

fibo_list = []

for i in range(0, n + 1):
    sum = numb2 - numb1
    numb2 = numb1
    numb1 = sum
    fibo_list.append(numb1)
    new_list = fibo_list[::-1]

for i in range(1, n + 1):   
    sum = numb3 + numb4
    numb3 = numb4
    numb4 = sum
    new_list.append(numb4)

print(new_list)