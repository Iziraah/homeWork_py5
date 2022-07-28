def get_win(win):
    win = 0
    if (pole[0][0] == pole[0][1] == pole[0][2] == "x" or 
        pole[1][0] == pole[1][1] == pole[1][2] == "x" or 
        pole[2][0] == pole[2][1] == pole[2][2] == "x" or
        pole[0][0] == pole[1][0] == pole[2][0] == "x" or
        pole[0][1] == pole[1][1] == pole[2][1] == "x" or
        pole[0][2] == pole[1][2] == pole[2][2] == "x" or
        pole[0][2] == pole[1][2] == pole[2][2] == "x" or
        pole[0][0] == pole[1][1] == pole[2][2] == "x" or
        pole[2][0] == pole[1][1] == pole[0][2] == "x"):
        win = 1
    elif (pole[0][0] == pole[0][1] == pole[0][2] == "o" or 
        pole[1][0] == pole[1][1] == pole[1][2] == "o" or 
        pole[2][0] == pole[2][1] == pole[2][2] == "o" or
        pole[0][0] == pole[1][0] == pole[2][0] == "o" or
        pole[0][1] == pole[1][1] == pole[2][1] == "o" or
        pole[0][2] == pole[1][2] == pole[2][2] == "o" or
        pole[0][2] == pole[1][2] == pole[2][2] == "o" or
        pole[0][0] == pole[1][1] == pole[2][2] == "o" or
        pole[2][0] == pole[1][1] == pole[0][2] == "o"):
        win = 1
    return win
pole = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
for i in range(0, len(pole)):
    for j in range(0, len(pole[i])):
        print(pole[i][j], end=' ')
    print()
def game(pole):
    print('Ход крестиком')
    i, j = list(map(int, input('Введите координаты через пробел: ').split()))
   
    if pole[i][j] == '-':
        pole[i][j] = "x"
    else:
        print('Клетка занята! ходи еще раз')
        i, j = list(map(int, input('Введите координаты через пробел: ').split()))
        pole[i][j] = "x"
    for i in range(0, len(pole)):
        for j in range(0, len(pole[i])):
            print(pole[i][j], end=' ')
        print()
    if get_win(pole) == 1:
        print('Победа игрока номер раз')
    elif get_win(pole) == 0:
        print('Ход ноликом')
        i, j = list(map(int, input('Введите координаты через пробел: ').split()))
        
        if pole[i][j] == '-':
            pole[i][j] = "o"
        else:
            print('Клетка занята! ходи еще раз')
            i, j = list(map(int, input('Введите координаты через пробел: ').split()))
            pole[i][j] = "o"
        for i in range(0, len(pole)):
            for j in range(0, len(pole[i])):
                print(pole[i][j], end=' ')
            print()
        if get_win(pole) == 1:
            print('Победа игрока номер два')
        elif get_win(pole) == 0:
            game(pole)
game(pole)
