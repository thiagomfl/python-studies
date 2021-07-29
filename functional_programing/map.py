list_1 = [1,2,3]
double = map(lambda x: x * 2, list_1)
print(list(double))

list_2 = [
  {'name': 'John', 'age': 31},
  {'name': 'Mary', 'age': 37},
  {'name': 'Joseph', 'age': 26}
]
only_names = map(lambda p: p['name'], list_2)
print(list(only_names))
only_ages = map(lambda p: p['age'], list_2)
print(sum(only_ages))

phrases = map(lambda p: f'{p["name"]} has {p["age"]} years old.', list_2)
print(list(phrases))
