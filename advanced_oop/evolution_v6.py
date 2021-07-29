from abc import ABCMeta, abstractproperty

# this define that this class is abtract
class Human(metaclass=ABCMeta):
    # class Atribute
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    @abstractproperty
    def intelligent(self):
        pass

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
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

    @property
    def intelligent(self):
        return False


class Sapiens(Human):
    specie = Human.species()[-1]
    
    @property
    def intelligent(self):
        return True


if __name__ == '__main__':
    try:
        anonymous = Human('John Doe')
        print(anonymous.intelligent)
    except TypeError:
        print('Abtract class')

    joseph = Sapiens('Joseph')
    print('{} from class {}, intelligent: {}'.format(joseph.name, joseph.__class__.__name__, joseph.intelligent))
    
    grokn = Neanderthal('Grokn')
    print('{} from class {}, intelligent: {}'.format(grokn.name, grokn.__class__.__name__, grokn.intelligent))
   