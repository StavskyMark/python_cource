'''
Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
превосходящие числа N
'''

number = int(input('Введите число: '))
degree = 1
while 2 ** degree <= number:
    print(f'2 в {degree} степени = {2 ** degree}')
    degree += 1
