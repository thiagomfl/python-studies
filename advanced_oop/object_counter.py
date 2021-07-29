class SimpleClass:
    counter = 0

    def __init__(self):
        self.counter()

    @classmethod
    def counter(cls):
        cls.counter += 1


if __name__ == '__main__':
    _list = [SimpleClass(), SimpleClass(), SimpleClass()]
    print(SimpleClass.counter)
