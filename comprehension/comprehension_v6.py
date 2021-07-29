def get_type_day(day):
    days = {
        (1, 7): 'Weekend',
        tuple(range(2, 7)): 'Workdays'
    }

    choosen_day = (_type for numbers, _type in days.items() if day in numbers)
    return next(choosen_day, '*** Invalid day ***')


if __name__ == '__main__':
    for day in range(0,9):
        print(f'{day}: {get_type_day(day)}')
