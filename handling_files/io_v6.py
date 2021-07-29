with open('persons.csv') as file:
    with open('persons.txt', 'w') as output:
        for record in file:
            person = record.strip().split(',')
            print('Id: {}, First Name: {}, Last Name: {}, Email: {}, Gender: {}, Ip Addresses: {}'.format(*person), file=output)

if file.closed:
    print('The file has already been closed!')
