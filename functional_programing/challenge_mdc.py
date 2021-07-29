def mdc(numbers): 
    def calc(divider):
        return divider if sum(map(lambda x: x % divider, numbers)) == 0 else calc(divider - 1)

    return calc(min(numbers))


if __name__ == '__main__':
    print(mdc([21, 7])) # 7
    print(mdc([125, 40])) # 5
    print(mdc([9, 563, 66, 3])) # 3
    print(mdc([55, 22])) # 11
    print(mdc([15, 150])) # 15
    print(mdc([7, 9])) # 1
