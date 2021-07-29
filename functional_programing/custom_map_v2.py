def mapping(fn, _list):
    return (fn(element) for element in _list)


if __name__ == '__main__':
    print(list(mapping(lambda x: x ** 2, [2, 3, 4])))
