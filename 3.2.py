# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def pairs_mult(list):
    mult_list = []
    index = len(list)
    
    for i in range(index):
        if index > i:
            index = index - 1
            mult_list.append(list[i]*list[index])

    print(mult_list)

list = [2, 3, 4, 5, 6]

pairs_mult(list)
