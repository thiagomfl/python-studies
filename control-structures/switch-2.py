def get_type_day(day):
    days = {
      1: 'weekend',
      2: 'workday',
      3: 'workday',
      4: 'workday',
      5: 'workday',
      6: 'workday',
      7: 'weekend',
    }

    return days.get(day, '** Invalid **')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_type_day(day)}')
