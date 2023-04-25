# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n (само число)

number = int(input('Enter a number: '))

def find_simple(number):
    count = 0
    for i in range(1, number + 1):
        if count > 2:
            break
        elif number % i == 0:
            count += 1
    return True if count <= 2 or number == 1 else False
print(find_simple(number))

def is_simple(number):
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True
print(is_simple(number))

