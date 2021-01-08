from sys import argv
_,hours,rate,premium =argv

print(f'зарплата составляет:{hours}*{rate}+{premium}-{float(hours)*float(rate)+float(premium)}')