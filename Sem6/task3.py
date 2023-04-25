# Задача №43
# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:
# 1 2 3 2 3

# Вывод:
# 2

def list_create_random(begin_num, end_num, length):
    import random
    return [random.randint(begin_num, end_num) for _ in range(length)]

def count_couple(number):
    # if number == 2:
    #     return 1
    # elif number < 2:
    #     return 0
    # else:
    #     return count_couple(number - 1) + (number - 1)
    if number < 2:
        return 0
    else:
        return 1 if number == 2 else count_couple(number - 1) + (number - 1)

def couple_val_list(list):
    result = 0
    set_list = set(list)
    for i in set_list:
        result += count_couple(list.count(i))
    return result

len_list = int(input('Enter a number-length for list: '))
my_list = list_create_random(1, 9, len_list)
print(*my_list)
print(couple_val_list(my_list))
