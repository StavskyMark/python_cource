'''
Задача 10:
 На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
некоторые – гербом. Определите минимальное число монеток, которые нужно
перевернуть, чтобы все монетки были повернуты вверх одной и той же
стороной. Выведите минимальное количество монет, которые нужно
перевернуть.

'''

count_monet = int(input('Введите количество монет: '))
count_eagle = 0
count_tails = 0
for i in range(count_monet):
    x = int(input('орел цифра 0, решка цифра 1: '))
    if x == 0:
        count_eagle += 1
    else:
        count_tails += 1

if count_tails > count_eagle:
    print(f'Минимальное количество монеток орлом вверх {count_eagle}')
else:
    print(f'Минимальное количество монеток решкой вверх {count_tails}')
