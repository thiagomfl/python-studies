class Human:
    # class Atribute
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError('Age must be a positive number!')
        
        self._age = age

    def from_caves(self):
        self.species = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def species():
        adjectives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjectives)

    @classmethod
    def is_evolved(cls):
        return cls.species == cls.species()[-1]


class Neanderthal(Human):
    specie = Human.species()[-2]


class Sapiens(Human):
    specie = Human.species()[-1]


if __name__ == '__main__':
    joseph = Sapiens('Joseph')
    joseph.set_age(40)
    print(f'Name: {joseph.name} Age: {joseph.get_age()}')
    
    grokn = Neanderthal('Grokn')

   