from itertools import count,cycle
print('итератор,генерирущие целые числа, начмная с указанного')
start= int(input('ввидите число, с которого начать генерацию:'))
end = int(input('Ввидите число, на котором следует остановиться:'))


counter=count(start)
for i in range(start, end+1):
    print(next(counter))

cycle = cycle([1,2,3])
action = None
print('итератор, повторяющийся элемент некторого списка, определенного заранее')
print('жми p, чтобы остановиться или любую другую кнопку чтобы продолжить')
while action !='p':
    print(next(cycle),end='')
    action = input()
