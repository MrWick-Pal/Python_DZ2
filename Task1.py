def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите вещественное число: ')
print(f'Сумма цифр в числе = {sum_digits(num)}')