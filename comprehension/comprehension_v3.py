generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))

# Versão "normal"
doubles = []
for i in range(11, 21):
    if i % 2 == 0:
        doubles.append(i * 2)

print(doubles)
