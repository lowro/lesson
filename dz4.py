a = float(int(input('ввидите расстояние в км, сколько пробежал спортсмен в первый день:')))
b = float(int(input('ввидите расстояние в км, сколько нужно достичь спортсмену:')))

counter = 1
while a <= b:
    print(f'{counter} день: {round(a, 2)} км.')
    a *= 1.1
    counter
print(f'{counter} день: {round(a, 2)} км.')
print(f'спортсмен пробежал не менее {b} км на {counter} день')