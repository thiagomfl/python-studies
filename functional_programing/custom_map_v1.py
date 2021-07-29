def mapping(fn, _list):
    for element in _list:
        yield fn(element)


if __name__ == '__main__':
    print(list(mapping(lambda x: x ** 2, [2, 3, 4])))
