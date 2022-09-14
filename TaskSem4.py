""" 
1. Вычислить число c заданной точностью d

Пример:

- при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10} 
"""

""" n = float(input('enter a real number: '))
d = float(input('enter d = '))
s = str(d)
print(round(n , abs(s.find('.') - len(s)) - 1)) """

###########################################################################

""" 
2.Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N. 
"""
#     Через SymPy
# from sympy import primefactors
# p = int(input('Введите натуральное число: '))
# primefactors_n = primefactors(n)
# print('Простые множители числа ', n,' = ', primefactors_n)

#     Без SymPy

# n = int(input('Введите натуральное число: '))
# prime_nums = []
# for i in range(2,n):
#     d = 2
#     while i % d != 0:
#         d += 1
#     if i == d and n%i == 0:
#         prime_nums.append(i)
# print('Простые множители числа ',n,' : ', prime_nums)

""" 
3.Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
"""
# lst = list(map(int, input("Enter the numbers separated by a space: ").split()))
# print(lst)
# nonrep_list = []
# [nonrep_list.append(i) for i in lst if i not in nonrep_list]
       
# print('Неповторяющиеся числа: ', nonrep_list)

""" 
4.Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k. 


Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
from random import randint
import itertools

k = randint(2, 8)

def rand_coef(k):
    coef = [randint(0, 100) for i in range (k + 1)]
    while coef[0] == 0:
        coef[0] = randint(1, 100) 
    return coef

def create_multinom(k, coef):
    value = ['*x^']*(k-1) + ['*x']
    multinom = [[a, b, c] for a, b, c  in itertools.zip_longest(coef, value, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in multinom:
        x.append(' + ')
    multinom = list(itertools.chain(*multinom))
    multinom[-1] = ' = 0'
    return "".join(map(str, multinom)).replace(' 1*x',' x')


coef = rand_coef(k)
multinom = create_multinom(k, coef)
print(multinom)

with open('multinom.txt', 'w') as formula:
    formula.write(multinom)



""" 
5.Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов. 
"""
