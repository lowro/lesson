def funcshan(a,b,c):
    digits = [a,b,c]
    max_elem = max(digits)
    digits.remove(max_elem)
    return max_elem + max(digits)
print(funcshan(1,3,5))