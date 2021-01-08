import operator
from functools import  reduce
print(reduce(operator.mul, [digit for digit in range(100,1001) if digit%2==0]))