person = {
  'name': 'Thiago',
  'age': 28,
  'role': 'Software Engineer',
  'techs': ['Javascript', 'Python']
}

type(person)
dir(dict)
len(person)

person['age']
person['name']
person['role']
person['techs']
person['techs'][1]
person.keys()
person.values()
person.items()
person.get('age')
person.get('tags')
person.get('tags', [])
person['techs'].append('PHP')
person.pop('age')
person.update({ 'age': 29, 'gender': 'M' })
del person['techs']

print(person)

