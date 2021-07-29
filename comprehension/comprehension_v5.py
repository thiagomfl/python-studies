dictionary = {i: i ** 2 for i in range(10) if i % 2 == 0}
print(dictionary)

for num, double in dictionary.items():
    print(f'{num} x 2 = {double}')
