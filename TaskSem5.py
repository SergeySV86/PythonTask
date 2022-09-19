""" 1.Напишите программу, удаляющую из текста все слова, содержащие "абв". """

# some_text = 'Напишите программу, удаляющую из текста все слова абвгдейки, содержащие "абв"'

# def delete_elems(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)

# res_text = delete_elems(some_text)
# print(some_text)
# print(res_text)

""" 2.Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом"" """

###### вариант двумя игроками:

# from random import randint

# def input_candy(name):
#     x = int(input(f"{name}, возьмите (введите количество) от 1 до 28 конфет: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите от 1 до 28: "))
#     return x


# def move_info(name, k, value):
#     print(f"{name} взял {k} шт. На столе осталось {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# all_candy = int(input("Введите начальное количество конфет на столе: "))
# move = randint(0,2) # чей ход
# if move:
#     print(f"Начинает {player1}")
# else:
#     print(f"Начинает {player2}")

# while all_candy > 28:
#     if move:
#         took_candy = input_candy(player1)
#         all_candy -= took_candy
#         move = False
#         move_info(player1, took_candy, all_candy)
#     else:
#         took_candy = input_candy(player2)
#         all_candy -= took_candy
#         move = True
#         move_info(player2, took_candy, all_candy)

# if move:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

###### вариант против рандомного бота:

# from random import randint

# def input_candy(name, col):
#     col = int(input(f"{name}, возьмите от 1 до {col} конфет): "))
#     while col < 1 or col > col:
#         col = int(input(f"Ошибка! Возьмите от 1 до {col}: "))
#     return col

# def move_info(name, k, value):
#     print(f"{name} взял {k} шт. На столе осталось {value} конфет.")

# def max_candy(col):
#     x = int(input(f"Сколько конфет можно взять за один раз (не более {col//2 - 1} ): "))
#     while col/2 < x:
#         x = int(input(f"Ошибка! Максимальное кол-во конфет за ход должно быть меньше {col//2}: "))
#     return x

# player1 = input("Введите имя первого игрока: ")
# player2 = "бот Вася"
# print(f"Против Вас играет {player2}")
# all_candy = int(input("Введите начальное количество конфет на столе: "))


# max_take = max_candy(all_candy)
# move = randint(0,2) # чей ход
# if move:
#     print(f"Начинает {player1}")
# else:
#     print(f"Начинает {player2}")

# while all_candy > max_take:
#     if move:
#         took_candy = input_candy(player1, max_take)
#         all_candy -= took_candy
#         move = False
#         move_info(player1, took_candy, all_candy)
#     else:
#         took_candy = randint(1,max_take+1)
#         all_candy -= took_candy
#         move = True
#         move_info(player2, took_candy, all_candy)

# if move:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# Вариант против бота посложнее

from random import randint
def input_candy(name, col):
    x = int(input(f"{name}, возьмите от 1 до {col} конфет: "))
    while x < 1 or x > col:
        x = int(input(f"Ошибка! Возьмите от 1 до {col}: "))
    return x

def move_info(name, k, value):
    print(f"{name} взял {k} шт. На столе осталось {value} конфет.")

def max_candy(col):
    x = int(
        input(f"Сколько конфет можно взять за один раз (менее {col//3} ): "))
    while col//3 <= x:
        x = int(input(
            f"Ошибка! Максимальное кол-во конфет за ход должно быть меньше {col//3}: "))
    return x

player1 = input("Введите имя первого игрока: ")
player2 = "бот Вася"
print(f"Против Вас играет {player2}")
all_candy = int(input("Введите начальное количество конфет на столе: "))


max_take = max_candy(all_candy)
move = randint(0, 2)  # чей ход
if move:
    print(f"Начинает {player1}")
else:
    print(f"Начинает {player2}")

while all_candy > max_take:
    if move:
        took_candy = input_candy(player1, max_take)
        all_candy -= took_candy
        move = False
        move_info(player1, took_candy, all_candy)
    else:
        if all_candy >= max_take * 2 + 1:
            took_candy = max_take
        else:
            if all_candy > max_take+1:
                took_candy = all_candy - max_take - 1
            else:
                took_candy = all_candy-1    
        all_candy -= took_candy    
        move = True       
        move_info(player2, took_candy, all_candy)        

if move:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")


""" 3.Создайте программу для игры в ""Крестики-нолики"". """


""" 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 

Входные и выходные данные хранятся в отдельных текстовых файлах."""
