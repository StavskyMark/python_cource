'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два
прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

n = int(input('Введите размер n: '))
m = int(input('Введите размер m: '))
k = int(input('Введите сколько долек хотите отломить: '))

if k % 2 == 0 and m * n != k:
    print(f'шоколадка размером {n} x {m} может быть разломана на {k} долек')
else:
    print(f'шоколадка размером {n} x {m} не может быть разломана на {k} долек')