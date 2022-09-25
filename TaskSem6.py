""" 1. Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.    
Добавьте возможность использования скобок, меняющих приоритет операций.        
*Пример:*        
1+2*3 => 7;         
(1+2)*3 => 9; """ 

input_string = input('Введите пример: ')
list_of_operators = ['-', '+', '*', '/']


def restriction_by_brackets(s):
    if "(" in s:
        s = s.replace(s[s.index('('):],
        restriction_by_brackets(s[s.index('(') + 1:]))
    if ")" in s:
        s = s.replace(s[0:s.index(')') + 1],
        str(split_into_arfim(s[0:s.index(')')])))
        return s
    return split_into_arfim(s)


def split_into_arfim(str, op = ['-', '+', '*', '/']):
    ops_lst = []
    nums = []
    temp = ''
    for char in str:
        if not char in op:
            temp += char
        else:
            ops_lst.append(char)
            try:
                nums.append(float(temp))
            except:
                print('error symbol')
                exit()
            temp = ''
    nums.append(float(temp))
    while len(nums) > 1:
        if '*' in ops_lst:
            i = ops_lst.index('*')
            temp = operation(nums[i], nums[i + 1], '*')
            nums[i] = temp
        elif '/' in ops_lst:
            i = ops_lst.index('/')
            temp = operation(nums[i], nums[i + 1], '/')
            nums[i] = temp
        elif '+' in ops_lst:
            i = ops_lst.index('+')
            temp = operation(nums[i], nums[i + 1], '+')
            nums[i] = temp
        elif '-' in ops_lst:
            i = ops_lst.index('-')
            temp = operation(nums[i], nums[i + 1], '-')
            nums[i] = temp
        del (nums[i + 1])
        del (ops_lst[i])
    return nums[0]


def operation(n1, n2, op):
    try:
        if op == '+':
            return n1 + n2
        if op == '-':
            return n1 - n2
        if op == '*':
            return n1 * n2
        if op == '/':
            try:
                return n1 / n2
            except:
                print('Division by zero')
                exit()
    except:
        print('Error value')
        exit()


print(input_string)
print(restriction_by_brackets(input_string))     

""" 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

*Пример:* 

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] """

# check_list = [1, 2, 3, 5, 1, 5, 3, 10]

# def find_unic_nums(lst): # через срез
#     unic_list = []
#     for i in range(len(lst)):
#         if lst[i] not in lst[i+1:] and lst[i] not in lst[:i]:
#             unic_list.append(lst[i])
#     return unic_list

# print(find_unic_nums(check_list))


# def find_unic_nums(lst): # через счетчик одинаковых
#     unic_list = []
#     for i in range(len(lst)):
#         if lst.count(lst[i]) == 1:
#             unic_list.append(lst[i])
#     return unic_list

# print(find_unic_nums(check_list))

