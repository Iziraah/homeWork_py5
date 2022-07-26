import random


print('на столе 101 конфет, сколько возьмешь?')
#x = int.input()
all = 100

def sweet(all):
    if all != 0:
        print('Сколько возьмешь? от 1 до 28')
        x = int(input())
        if x>28:
            print('Жулик! Бери меньше')
            sweet(all)
        if x<all:
            all -=x
            print('Остаток: ', all)
            y = all%29
            if y<all:
                print('Я взял: ', y)
                all -= y
                print('Остаток: ', all)
            if y == all: 
                print("я выиграл, бе-бе-бе")
                all -=y
            if all>0: sweet(all)
              
        if x == all: print("ты выиграл")
    elif all == 0:
        print("the end")
sweet(all)