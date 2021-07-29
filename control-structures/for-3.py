product = {
  'name': 'Caneta Bic',
  'price': 14.99,
  'imported': True,
  'stock': 784
}

for key in product:
    print(key)

for value in product.values():
    print(value)

for key, value in product.items():
    print(key, '=', value)

print(key, value)
