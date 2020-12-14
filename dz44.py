number = int(input('ввидите целое положительное число:'))

str_number =str(number)

i = 0

temp = 0
while i != len(str_number):
    if int(str_number[i]) == 11:
        temp = 11
        break
    if int(str_number[i]) > temp:
        temp = int(str_number[i])
        i += 1
print(f'максимальная цифра в числе {number} - {temp}')