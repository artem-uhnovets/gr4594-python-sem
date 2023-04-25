# Задача №45
# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1,
# но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10**5.
# Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).

# Ввод: 300

# Вывод: 220 284

def dict_create(end_range):
    dict = {}
    for i in range(2, end_range + 1):
        summ_i = 0
        for j in range(1, (i // 2) + 1):
            summ_i = summ_i + j if i % j == 0 else summ_i
        dict[i] = summ_i
    return dict

def dict_friendly_values(source_dict):
    set_values = set()
    for i in range(2, len(source_dict)):
        for j in source_dict.values():
        # for j in range(len(source_dict)):
            if i == source_dict.get(j) and j == source_dict.get(i) and i != j:
                set_values.add(i)
                set_values.add(j)
    return set_values

number = int(input('Enter a number K: '))
dict = dict_create(number)
print(*dict_friendly_values(dict))

result_list = list(dict_friendly_values(dict))
print(result_list)
for i in range(len(result_list) - 1):
    if result_list[i] < result_list[i + 1]:
        print(result_list[i], result_list[i + 1])