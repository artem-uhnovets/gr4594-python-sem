""" 
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
"""

stroka = input('Enter a letters: ').lower()
list = stroka.split()
set = set(list)
dic = {i: 0 for i in set}

for i in range(len(list)):
    if list[i] in dic:
        print(list[i] if dic[list[i]] == 0 else f'{list[i]}_{dic[list[i]]}', sep ='', end =' ')
        dic[list[i]] += 1
        # if dic[list[i]] == 0:
        #     print(list[i], sep ='', end =' ')
        #     dic[list[i]] += 1
        # else:
        #     print(f'{list[i]}_{dic[list[i]]}', sep ='', end =' ')
        #     dic[list[i]] += 1
