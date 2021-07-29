class Human:
    # class Atribute
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

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
    grokn = Neanderthal('Grokn')

    print(f'Evolution (from class): {", ".join(Sapiens.species())}')
    print(f'Evolution (from instance): {", ".join(joseph.species())}')
    print(f'Homo Sapiens is evolved? {Sapiens.is_evolved()}')
    print(f'Neanderthal is evolved? {Neanderthal.is_evolved()}')
    print(f'Joseph is evolved? {joseph.is_evolved()}')
    print(f'Grokn is evolved? {grokn.is_evolved()}')
