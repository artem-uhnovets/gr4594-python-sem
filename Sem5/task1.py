# Последовательностью Фибоначчи
# последовательность чисел a0, a1, ..., an, ..., где
# a(0) = 0, a(1) = 1, a(k) = a(k-1) + a(k-2)(k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# Задание необходимо решать через рекурсию

# def fibo1(number):
#     list = []
#     list.append(1)
#     list.append(1)
#     for i in range(2, number + 1):
#         list.append(list[i - 1] + list[i - 2])
#     return list[number]

# number = int(input('Enter a number: '))
# print(fibo1(7))

# def fibo2(number):
#     count = 2
#     a, b = 1, 1
#     while count <= number:
#         result = a + b
#         b = a
#         a = result
#         count += 1
#     return result

# number = int(input('Enter a number: '))
# print(fibo2r(7))

def fibo_recur(number):
    while number >= 2:
        return fibo_recur(number - 1) + fibo_recur(number - 2)
    else:
        return 1

number = int(input('Enter a number: '))
print(fibo_recur(number))


