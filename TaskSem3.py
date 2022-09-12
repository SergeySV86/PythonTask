"""
1. Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

""" 
lst_nums = []
n = int(input('Введите длину массива: '))
for i in range(n):
    lst_nums.append(int(input('Введите число: ')))
print(lst_nums)
print('Элементы стоящие на нечетных позициях: ')
for i in range(1, len(lst_nums), 2):
   print(lst_nums[i], end=' ' )

# функция суммы всех элементов на нечетных позициях
def SumOdds(list):
    return sum(list[i] for i in range(1, len(list), 2))

print('cумма этих элементов: ', SumOdds(lst_nums))
 """
############################################################
""" 
2.Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

""" 
lst_nums = []
n = int(input('Введите длину массива: '))
for i in range(n):
    lst_nums.append(int(input('Введите число: ')))
print(lst_nums)

def numsMult(lst_nums):
    res = []
    while len(lst_nums) > 1:
        res.append(lst_nums[0]*lst_nums[-1])
        del lst_nums[0] 
        del lst_nums[-1] 
    if len(lst_nums) == 1: res.append(lst_nums[0]**2)       
    return res

print(numsMult(lst_nums)) 
"""
##################################################################

""" 
3.Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

""" 
lst = list(map(float, input("Enter the numbers separated by commas:\n").split(', ')))
result = [round(i%1,2) for i in lst if i%1 != 0]
diff = max(result) - min(result)
print(round(diff,2))   
"""     
###################################################################

""" 
4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 
"""

""" 
string = ''
dec = int(input('Enter a decimal number: '))
num = dec
while num != 0:
    string = str(num % 2) + string
    num //= 2
print('Decimal number ', dec, ' is binary number ',string)
 
"""
###############################################################

""" 
5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

""" 
k = int(input('k = '))

def negafibo(k):
    fibonacci = []
    a, b = 1, 1
    for i in range(k):
        fibonacci.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k+1):
        fibonacci.insert(0, a)
        a, b = b, a - b
    return fibonacci

negafibonacci = negafibo(k)
print(negafibo(k), '\n' ) 
"""

    