def vozv(x:float, y:int):
    res = 1
    for i in range(abs(y)):
        res *= x
        return x ** y, 1 /res
print(vozv(4.5, -4))