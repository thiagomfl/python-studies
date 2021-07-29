from function_first_class import double, square


def process(title, list, fn):
    print(f'Processing: {title}')
    for i in list:
        print(i, '=>', fn(i))


if __name__ == '__main__':
    process('Double from 1 to 10', range(1, 11), double)
    process('Squares from 1 to 10', range(1, 11), square)
