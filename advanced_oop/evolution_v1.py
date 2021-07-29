class Human:
    # class Atribute
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def from_caves(self):
        self.species = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    joseph = Human('Joseph')
    grokn = Human('Grokn').from_caves()

    print(f'Human.specie: {Human.species}')
    print(f'joseph.specie: {joseph.species}')
    print(f'grokn.specie: {grokn.species}')
