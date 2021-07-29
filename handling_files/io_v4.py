# Esta versão é feito streaming do arquivo pelo Python

try:
    file = open('persons.csv')
    
    for record in file:
        print('Id: {}, First Name: {}, Last Name: {}, Email: {}, Gender: {}, Ip Addresses: {}'.format(*record.strip().split(',')))
except IndexError:
    pass       
finally:
    file.close()

if file.closed:
    print('The file has already been closed!')
