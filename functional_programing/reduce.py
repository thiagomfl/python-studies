from functools import reduce

persons = [
    {'name': 'Pedro', 'age': 11},
    {'name': 'Rebeca', 'age': 6},
    {'name': 'Arthur', 'age': 26},
    {'name': 'Thiago', 'age': 28},
    {'name': 'Mariana', 'age': 18},
    {'name': 'Gabriela', 'age': 17},
]

only_ages = map(lambda p: p['age'], persons)
minors = filter(lambda p: p['age'] < 18, only_ages)
sum_ages = reduce(lambda ages, age: ages + age, minors, 0)
print(sum_ages)
