# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

my_list = [1, 3, 4, 3, 4, 4, 4]
def swap (list):
    for i in range(list.count(max(list))):
        list[list.index(max(list))] = min(list)
    return list
print(swap(my_list))
