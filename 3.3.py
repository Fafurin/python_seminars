# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def max_min_diff(list):
    new_list = []
    
    for i in range(len(list)):
        new_list.append(list[i] - int(list[i]))

    print(max(new_list) - min(new_list))

list = [1.1, 1.2, 3.1, 5, 10.01]

max_min_diff(list)
