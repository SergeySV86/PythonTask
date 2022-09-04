""" 
1.Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:
- 6 -> да
- 7 -> да
- 1 -> нет 

num_day = int(input('Enter the number indicating the day of the week: '))
if num_day == 6 or num_day == 7:
    print('Yes')
else:
    print('No')

"""
###########################################################################
"""
2.Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 

x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))
if not(x + y + z) == (not(x)) * (not(y)) * (not(z)):
    print('true') 
else:
    print('false')

"""
##############################################################################
""" 
3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 


x = int(input('Enter x: '))
y = int(input('Enter y: '))
if x > 0 and y > 0:
    print('Point in the 1-st quarter')
if x < 0 and y > 0:
    print('Point in the 2-nd quarter')
if x < 0 and y < 0:
    print('Point in the 3-d quarter')
if x > 0 and y < 0:
    print('Point in the 4-th quarter')
if x == 0 or y == 0:
    print('x or y cannot to be 0')

"""
###########################################################
"""
4.Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).


num_q = int(input('Enter the number of the quarter: '))
if num_q == 1:
    print('x > 0 and y > 0')
if num_q == 2:
    print('x < 0 and y > 0')
if num_q == 3:
    print('x < 0 and y < 0')
if num_q == 4:
    print('x > 0 and y < 0')
if num_q <= 0 or num_q > 4:
    print('False')

"""
##################################################################

"""
5.Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
xA = int(input())
yA = int(input())
xB = int(input())
yB = int(input())

dist = ((xA - xB)**2 + (yA - yB)**2)**(1/2)
print(round(dist,2))
print(f'{dist:.2f}')
print("%.2f" % dist)

