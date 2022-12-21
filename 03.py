# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
print('введите число - ')
n = int(input())
list = []
for i in range(n):
    list.append(randint(-n, n))
print (list)

with open('file.txt','w') as posicn:
    posicn.write('1\n')
    posicn.write('2\n') 
    posicn.write('3\n') 


posicn = open('file.txt','r')
result = list[int(posicn.readline(1))] * list[int(posicn.readline(3))]
print(result)