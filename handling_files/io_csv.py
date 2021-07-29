import csv

with open('persons.csv') as inputi:
    for person in csv.reader(inputi):
        print('Id: {}, First Name: {}, Last Name: {}, Email: {}, Gender: {}, Ip Addresses: {}'.format(*person))
