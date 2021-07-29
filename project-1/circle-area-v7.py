from math import pi


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    radius = input('Inform the radius: ')
    area = circle(radius)
    print('Circle area is', area)
