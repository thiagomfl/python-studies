LEGAL_AGE = 18


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        if not self.age:
            return self.name

        return f'{self.name} ({self.age} years old)'

    def is_adult(self):
        return (self.age or 0) > LEGAL_AGE
