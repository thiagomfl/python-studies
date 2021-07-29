from generators_v1 import rainbow_colors

if __name__ == '__main__':
    generator = rainbow_colors()
    print(type(generator))

    for color in generator:
        print(color)

    print('the end...')
