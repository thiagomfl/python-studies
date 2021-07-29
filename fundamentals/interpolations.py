from string import Template

name, age = 'Thiago', 28.10
print('Nome: %s Idade: %.2f' % (name, age))
print('Nome: {0} Idade: {1}'.format(name, age))
print(f'Nome: {name} Idade: {age}')

s = Template('Nome: $name Idade: $age')
print(s.substitute(name=name, age=age))
