# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbs = [3, 5, 6, 2, 3, 5, 12, 6, 12]

def get_unique_numbers(numbs):
    unique = []

    for numb in numbs:
        if numb in unique:
            continue
        else:
            unique.append(numb)
    return unique

print(get_unique_numbers(numbs))