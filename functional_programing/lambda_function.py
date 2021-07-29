purchases = (
  {'qty': 2, 'price':10},
  {'qty': 4, 'price':20},
  {'qty': 3, 'price':15},
  {'qty': 6, 'price':30},
)

totals = tuple(map(lambda purchase: purchase['qty'] * purchase['price'], purchases))

print('Total prices:', totals)
print('Total General:', sum(totals))
