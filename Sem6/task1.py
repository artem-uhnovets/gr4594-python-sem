# Задача №39
# Даны два массива чисел.
# Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива.

# Ввод
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# Вывод:
# 3 3 2 12

def list_create_random(begin_num, end_num, length):
    import random
    return [random.randint(begin_num, end_num) for _ in range(length)]

def diff_lists(list_1, list_2):
    for i in range(len(list_1)):
        if list_2.count(list_1[i]) == 0:
            print(list_1[i], end=' ')

len_1st_list = int(input('Enter a number-length for 1st list: '))
list_1st = list_create_random(1, 9, len_1st_list)

len_2nd_list = int(input('Enter a number-length for 2nd list: '))
list_2nd = list_create_random(1, 9, len_2nd_list)

print(*list_1st)
print(*list_2nd)

diff_lists(list_1st, list_2nd)