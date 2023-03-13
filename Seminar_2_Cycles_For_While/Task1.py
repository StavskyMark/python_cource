'''
По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
(произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
'''

number1 = int(input('Введите число: '))
factorial = 1
number2 = number1
while number2 > 1:
    factorial *= number2
    number2 -= 1

print(f'факториал числа {number1} = {factorial}')
