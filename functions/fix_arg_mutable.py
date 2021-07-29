def fibonacci(sequence=None):
    sequence = sequence or [0, 1]
    sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == '__main__':
    init = fibonacci()
    print(init, id(init))
    print(fibonacci(init))

    restart = fibonacci()
    print(restart, id(restart))
    print(fibonacci(restart))
