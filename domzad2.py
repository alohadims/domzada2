n = int(input('Введите число n: '))
posled = []
for i in range(1,n+1):
    list_n = ((1+1/n)**n)
    posled.append(list_n)
print(f'Последовательность: {posled}')
print(f'Сумма: {sum(posled)}')