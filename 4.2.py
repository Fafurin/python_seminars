# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

numb = int(input("Введите натуральное число: "))

i = 2
res_list = []
while i * i <= numb:
    while numb % i == 0:
        res_list.append(i)
        numb = numb / i
    i = i + 1
if numb > 1:
    res_list.append(int(numb))
print(res_list)