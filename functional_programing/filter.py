persons = [
  {'name': 'Pedro', 'age': 11},
  {'name': 'Mariana', 'age': 18},
  {'name': 'Arthur', 'age': 26},
  {'name': 'Rebeca', 'age': 6},
  {'name': 'Thiago', 'age': 28},
  {'name': 'Gabriela', 'age': 17},
]

minors = filter(lambda p: p['age'] < 18, persons)
print(list(minors))

big_names = filter(lambda p: len(p['name']) >= 7, persons)
print(list(big_names))
