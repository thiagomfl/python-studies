print(dir(int))
print(dir(float))

a = 2
b = 2.5

print(a / b)
print(a + b)
print(a * b)

print(type(a))
print(type(b))
print(type(a - b))

print(1.1 + 2.2)

from decimal import Decimal, getcontext
Decimal(1) / Decimal(7)
getcontext().prec = 2
print(Decimal(1) / Decimal(7))