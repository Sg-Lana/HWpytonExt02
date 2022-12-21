# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# например, пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('введите число - ')
n = int(input())
factorial = 1
list = []
while n > 1:
    for i in range(1, n+1):
        factorial *= i
        list.append(factorial)
        n -= 1
print(list)
