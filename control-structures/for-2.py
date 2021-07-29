word = 'paralelepipedo'
for letter in word:
    print(letter, end=' ')

print('End')

approveds = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for name in approveds:
    print(name)

for position, name in enumerate(approveds):
    print(f'{position + 1})', name)

week_days = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')
for day in week_days:
    print(f'Hoje é {day}')

for letter in set('Thiago'):
    print(letter)
