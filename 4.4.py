# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

import random

degree = int(input("Введите степень: "))

polinom = ''

list = [i for i in range(0, 100)]

while degree > 0:
    polinom = polinom + str(random.choice(list)) + 'x^' + str(degree) + ' + '
    degree = degree - 1

print(polinom[:-5])