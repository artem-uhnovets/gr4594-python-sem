# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

# number = int(input('Enter a number: '))
def rev_inp(input_number):
    if input_number == 1:
        value = input()
        return value
    value = input()
    return rev_inp(input_number - 1) + ' ' + value
number = int(input('Enter a number: '))
print(f'Enter {number} value(s)')
print(rev_inp(number))