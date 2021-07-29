class HtmlToStringMixin:
    def __str__(self) -> str:
        html = super().__str__().replace('(', '<strong>(').replace(')', '</strong>)')
        return f'<span>{html}</span>'


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Animal:
    def __init__(self, name, pet=True):
        self.name = name
        self.pet = pet

    def __str__(self):
        return self.name + ' (pet)' if self.pet else ''


class PersonHtml(HtmlToStringMixin, Person):
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Person('Thiago Moura')
    print(p1)
    p2 = Person('Priscila Borges')
    print(p2)
    toto = Person('Rex')
    print(toto)
