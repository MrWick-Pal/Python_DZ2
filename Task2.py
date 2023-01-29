# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
n = int (input('Введите число N: '))
sum = 1
numbers = []
for i in range (1, n + 1):
    count = i*sum
    sum = count
    numbers += [count] 

print (numbers)