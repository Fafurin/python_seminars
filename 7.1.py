# 1. Здача про стишки Винни-Пуха

poem = input("Введите стихотворение Винни-Пуха на русском языке: ")

# считает гласные в строке, возвращает целое число или 0
def vowels_counting(string):
    count = 0
    vowels = set("АОУЫЭЕЁИЮЯаоуыэеёиюя")

    for letter in string:
        if letter in vowels:
            count += 1

    return count

# считает гласные в каждом слове фразы, возвращает список целых чисел
def word_comparison(string):
    list = string.split()
    
    vowels_list = []

    for word in list:
        vowels_list.append(vowels_counting(word))
    
    return vowels_list
    
# сравнивает значения списка, возвращает True либо False
def isEqual(list):
    return len(set(list)) <= 1
 
if (isEqual(word_comparison(poem))):
    print("Парам пам-пам")
else:
    print("Пам парам")