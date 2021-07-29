double_pairs = [i * 2 for i in range(10) if i % 2 == 0]
print(double_pairs)

# Versão "normal"
doubles = []
for i in range(11, 21):
    if i % 2 == 0:
        doubles.append(i * 2)

print(doubles)
