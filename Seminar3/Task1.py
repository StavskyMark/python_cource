import random

nunb_list = [random.randint(0, 20) for i in range(40)]

print(nunb_list)

numb_set = set(nunb_list)
print(numb_set)
print(len(numb_set))
