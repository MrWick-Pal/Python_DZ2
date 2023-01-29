# Задайте список из n чисел последовательности (1 + 1/n)**n 
# и выведите на экран их сумму.
n = int(input('Введите кол-во чисел в списке: '))
sum = 1
lst = []
for i in range(1, n+1):
    res = round((1 + 1/n)**n)
    sum += res
    lst += [sum]

print (lst)