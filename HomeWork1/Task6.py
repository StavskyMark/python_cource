'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых
трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''

number_ticket = int(input('Введите шестизначный номер билета: '))

sum_first = (number_ticket % 1000000 // 100000) + (number_ticket % 100000 // 10000) + (number_ticket % 10000 // 1000)
sum_last = (number_ticket % 1000 // 100) + (number_ticket % 100 // 10) + (number_ticket % 10)

if sum_first == sum_last:
    print(f'Билет с номером {number_ticket} счастливый!!')
else:
    print(f'Билет с номером {number_ticket} не счастливый!!')
