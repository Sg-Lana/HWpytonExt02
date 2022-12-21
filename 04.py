#Реализуйте алгоритм перемешивания списка.

import random
print('введите кол-во элементов списка -')
n = int(input())
list = []
for i in range(n):
    list.append(random.randrange(1,10))
print(list)
for i in range(len(list)-1, 0, -1):
        j = random.randint(0, i +1)
        list[i], list[j] = list[j], list[i]
print(list)