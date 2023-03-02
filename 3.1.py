# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def odd_el_sum(list):
    sum = 0

    for i in range(len(list)):
        if i%2 == 1:
            sum = sum + list[i]

    print(sum)

list = [2, 3, 5, 9, 3]

odd_el_sum(list)
