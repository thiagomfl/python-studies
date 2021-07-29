# print(dir(str))

name = "Thiago Moura"
print(name)
print(name[0])
print(name[-4])
print(name[4:])
print(name[-8:])
print(name[:3])

# name[0] = "P" can not use this case

print("Dias D'Avila" == 'Dias D\'Avila')
doc = """
  lorem * 20
"""
# print(doc)

numbers = '1234567890'
print(numbers[::])
print(numbers[::2])
print(numbers[1::2])
print(numbers[::-1])

phrase = "Python is awesome"
print('py' not in phrase)
print('aw' in phrase)
print(len(phrase))

a = '123'
b = ' de Lima 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a, b))

len(a)
a.__len__()
'1' in a
a.__contains__('1')
