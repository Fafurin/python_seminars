# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def rem_words():
    print("-- Программа, удаляюет из текста все слова, содержащие определенные символы --")
    text = input("Введите текст: ")
    chars = input("Введите запрещенные символы через пробел: ")

    test_list = text.split()

    char_list = chars.split()
    
    print ("Введенный текст :")
    print (test_list)
    print ("Запрещенные символы :")
    print (char_list)

    res = []
    flag = 1
    for ele in test_list:
        for idx in char_list:
            if idx not in ele:
                flag = 1
            else:
                flag = 0
                break
        if(flag == 1):
            res.append(ele)
    
    print ("Результат :")
    print (res)

rem_words()