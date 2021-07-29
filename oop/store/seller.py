from .person import Person


class Seller(Person):
    def __init__(self, name, age, wage):
        super().__init__(name, age)
        self.wage = wage
