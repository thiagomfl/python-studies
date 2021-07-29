def execute(fn):
    if callable(fn):
        fn()


def good_morning():
  print('Good Morning!')


def good_afternoon():
  print('Good Afternoon!')

if __name__ == '__main__':
    execute(good_morning)
    execute(good_afternoon)
    execute(1)
