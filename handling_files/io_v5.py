with open('persons.csv') as file:
    for record in file:
        print('Id: {}, First Name: {}, Last Name: {}, Email: {}, Gender: {}, Ip Addresses: {}'.format(*record.strip().split(',')))

if file.closed:
    print('The file has already been closed!')
