# 3. Создайте программу для игры в ""Крестики-нолики"".

print("Крестики-нолики")

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_field(field):
    print(" ----------------------- ")
    for i in range(3):
        print ("|  " , field[0+i*3], "  |  ", field[1+i*3], "  |  ", field[2+i*3], "  |")
        print(" ----------------------- ")

def take_move(move):
    valid = 0
    while not valid:
        player_move = int(input("Куда поставим " + move + "? "))
        if player_move >= 1 and player_move <= 9:
            if (str(field[player_move - 1]) not in "OX"):
                field[player_move - 1] = move
                valid = True
            else:
                print ("Это поле занято")
        else:
            print ("Введите число от 1 до 9.")

def check_win(field):
    win_comb = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_comb:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False

def start(field):
    counter = 0
    win = False
    while not win:
        print_field(field)
        if counter % 2 == 0:
            take_move("X")
        else:
            take_move("O")
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print(tmp, "Выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    print_field(field)

start(field)