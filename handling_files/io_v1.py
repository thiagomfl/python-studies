file = open('persons.csv')

data = file.read()
file.close()

for record in data.splitlines():
    print('Id: {}, First Name: {}, Last Name: {}, Email: {}, Gender: {}, Ip Addresses: {}'.format(*record.split(',')))
