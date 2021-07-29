from math import pi
import sys
import errno

class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circle(radius):
    return pi * float(radius) ** 2


def circleHelp():
    if sys.argv[1]:
        print(TerminalColor.ERRO + 'The radius must be a numerical value.' + TerminalColor.NORMAL)
    else:
        print(TerminalColor.ERRO + "It is necessary to inform the radius of the circle." + TerminalColor.NORMAL)

    print("Syntax: {} <radius>".format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        circleHelp()
        sys.exit(errno.EPERM)
    
    if not sys.argv[1].isnumeric():
        circleHelp()
        sys.exit(errno.EINVAL)
    
    radius = sys.argv[1]
    area = circle(radius)
    print('Circle area is', area)
