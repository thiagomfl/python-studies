from random import randint

# while True:
#     print('It\'s to long...')

informed_number = -1
secret_number = randint(0, 9)

while informed_number != secret_number:
    informed_number = int(input('Number: '))
  
print('Secret number {} was matched!'.format(secret_number))
