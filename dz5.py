earnings = float(input("ввидите значение выручки:"))
outgoings = float(input('ввидите значение издержки:'))

if earnings > outgoings:
    profit = earnings - outgoings
    print(f'фирма рабоатет в плюс, рентабельность выручки: {profit / earnings:.2f}')
    count_workers = int(input('ввидите количестово сотрудников:'))
    print(f'прибыль фирмы на одного сотрудника: {profit / count_workers}')
elif earnings < outgoings:
    print('фирма рабоатет в минус')
else:
    print('доходы и расходы равны')
