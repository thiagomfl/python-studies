print(True or False)  # //
print(7 != 3 and 2 > 3)  # &&

if (not False):
    print(2)

amount = 1000
wage = 6305
expenses = 4948

target = amount > 0 and wage - expenses >= 0.2 * wage
print(target)
