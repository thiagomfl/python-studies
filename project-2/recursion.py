def printy(max, actual):
    if actual < max:
      print(actual)    
      printy(max, actual + 1)


printy(100, 1)
