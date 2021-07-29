class _Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

        print('Hello!')


    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


d1 = _Date(28, 7, 2021)
# d1.day = 28
# d1.month = 7
# d1.year = 2021
print(d1)

d2 = _Date(29, 8, 2022)
# d2.day = 29
# d2.month = 7
# d2.year = 2021
print(d2)

d3 = _Date()
print(d3)

print(type(d3))
