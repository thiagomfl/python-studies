class _Date:
    def __str__(self):
        return f'{self.day}/{self.month}/{self.year}'


d1 = _Date()
d1.day = 28
d1.month = 7
d1.year = 2021
print(d1)

d2 = _Date()
d2.day = 29
d2.month = 7
d2.year = 2021
print(d2)
