# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233
# 0 1 2 3 4 5 6  7  8  9 10 11  12  13
# 1 2 3 4 5 6 7  8  9 10 11 12  13  14

number = input('Enter a number: ')
numPrev = 0
numCur = 1
numNext = 0
fibo = str(numPrev) + ' ' + str(numCur)
while int(number) >= numNext:
    numNext = numCur + numPrev
    fibo = fibo + ' ' + str(numNext)
    numPrev = numCur
    numCur = numNext
fibo = fibo.split(' ')
if number in fibo:
    print(fibo.index(number) + 1)
else:
    print(-1)

# print(fibo.index(number) + 1 if number in fibo else -1)

""" 
n = int(input("Введите число: "))
i = 1
a=0
b=1

while n>a:
    temp = a + b
    a = b
    b = temp
    i+=1
# else:
if (a==n): 
    print(f"Номер {i}")
else:
    print(f"Номер -1")

"""
""" 
n = int(input("Введите число: "))
f_i = 2
f_1 = 0
f_2 = 1

while f_2 < n:
    f_1, f_2 = f_2, f_1 + f_2
    f_i += 1

if (f_2 == n): 
    print(f"Номер {f_i}")
else:
    print(f"Номер -1")
"""