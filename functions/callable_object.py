class _Pow:
    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, base):
        return base ** self.exponent


if __name__ == '__main__':
    square = _Pow(2)
    cube = _Pow(3)

    if callable(square) and callable(cube):
        print(f'3² => {square(3)}')
        print(f'5³ => {cube(5)}')
        print(_Pow(4)(2))
