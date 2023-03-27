'''
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
'''

list_len = int(input('Введите длину последовательности: '))
shift = int(input('Введите величину сдвига: '))

my_list = [i for i in range(list_len)]
print(my_list)

'''
1 решение:
for i in range(shift):
    my_list.insert(0, my_list.pop())
print(my_list)
'''

'''
2 решение:
print(my_list[-shift:] + my_list[: -shift])
'''

''' 3 решение: '''

for i in range(len(my_list)):
    print(my_list[i - shift], end=' ')
