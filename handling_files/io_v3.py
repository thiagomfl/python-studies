# Esta versão é feito streaming do arquivo pelo Python

file = open('persons.csv')

for record in file:
    print('Id: {}, First Name: {}, Last Name: {}, Email: {}, Gender: {}, Ip Addresses: {}'.format(*record.strip().split(',')))

file.close()
