def multiply(x):
    def calc(y):
        return x * y

    return calc


if __name__ == '__main__':
    double = multiply(2)
    triple = multiply(3)
    print(double, triple)
    print(f'Double of 6 is {double(6)}')
    print(f'Triple of 3 is {triple(3)}')
