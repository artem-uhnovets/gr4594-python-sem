# Задача №41
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

def list_create_random(begin_num, end_num, length):
    import random
    return [random.randint(begin_num, end_num) for _ in range(length)]


def count_min_neigh_values(list):
    count = 0
    for i in range(1, len((list)) - 1):
        if list[i] > list[i - 1] and list[i] > list[i + 1]:
            count += 1
    return count

len_list = int(input('Enter a number-length for list: '))
list_1st = list_create_random(1, 9, len_list)
print(*list_1st)
print(count_min_neigh_values(list_1st))