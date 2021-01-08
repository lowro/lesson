name ='dz5.txt'
with open(name, 'w', encoding= 'UTF-8') as f:
    digits = input('ввидите набор чисел через пробел')
    f.write(digits)
with open(name, 'r', encoding= 'UTF-8') as f:
    digits_str = f.read()
    print(sum([int(digit) for digit in digits_str.split()]))