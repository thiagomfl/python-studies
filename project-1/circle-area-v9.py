from math import pi
import sys


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("It is necessary to inform the radius of the circle.")
        print("Syntax: {} <radius>".format(sys.argv[0]))
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print('Circle area is', area)
