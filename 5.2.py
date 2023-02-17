# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

import time
import random

player1_all_candies = 0
player2_all_candies = 0

candies = int(input("Введите количество конфет на столе: "))

valid = 0

def getCandies(player):
    global valid
    global candies
    global player1_all_candies
    global player2_all_candies

    while not valid:
        player_candies = int(input("Игрок № " + str(player) + " введите количество конфет от 1 до 28: "))

        if player_candies < 1 or player_candies > 28:
            print("Введите количество конфет от 1 до 28: ")
        else:
            if candies - player_candies == 0:
                print("Игрок № " + str(player) + " победил!")
                valid = 1
            elif candies - player_candies > 0:
                candies -= player_candies
                print("Переход хода")

                if (player == 1):
                    player1_all_candies += player_candies
                    print_info()
                    getCandies(2)
                    valid = 1
                else:
                    player2_all_candies += player_candies
                    print_info()
                    getCandies(1)
                    valid = 1
            elif candies - player_candies < 0:
                print("Недостаточно конфет на столе")

def print_info():
    print("Конфеты на столе: ")
    print(candies)
    print("------------------")
    print("Конфеты игрока № 1: ")
    print(player1_all_candies)
    print("------------------")
    print("Конфеты игрока № 2: ")
    print(player2_all_candies)

def start():
    if candies > 0:
        print("Жеребьевка...")
        print("-------------")
        time.sleep(2)

        player = random.randint(1,2)

        print("Начинает игрок № " + str(player))

        print_info() 
        getCandies(player)

start()