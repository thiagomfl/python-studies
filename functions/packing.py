def sum_2(a, b):
    return a + b


def sum_3(a, b, c):
    return a + b + c


def sum_n(*numbers):
    print(type(numbers))
    _sum = 0
    for n in numbers:
        _sum += n

    return _sum


if __name__ == '__main__':
    print(sum_2(2, 3))
    print(sum_3(2, 4, 6))

    # packing
    print(sum_n(1))
    print(sum_n(1, 2))
    print(sum_n(1, 2, 2, 3, 4, 5, 6))

    # unpacking
    tupla_nums = (1, 2, 3)
    print(sum_3(*tupla_nums))
    list_nums = [1, 2, 3]
    print(sum_3(*list_nums))

