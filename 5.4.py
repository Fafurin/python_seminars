# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(): 
    string = input("Введите строку для сжатия: ")
    result = '' 
    prev_char = '' 
    count = 1 

    for char in string: 
        if char != prev_char: 
            if prev_char: 
                result += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else: 
        result += str(count) + prev_char 
        return result

print(rle_encode())


def rle_decode():
    string = input("Введите строку для восстановления данных: ") 
    result = '' 
    count = '' 
    for char in string: 
        if char.isdigit(): 
            count += char 
        else: 
            result += char * int(count) 
            count = '' 
    return result

print(rle_decode())
