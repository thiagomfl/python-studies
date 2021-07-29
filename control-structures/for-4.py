from random import randint

for i in range(1, 10):
    if i == 6:
      break
    print(i)
else:
    print('Fim!')


def draw_dice():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if draw_dice() == i:
        print('ACERTOU', i)
        break
else:
    print('Nao acertou o numero!')
