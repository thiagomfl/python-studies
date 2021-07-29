FORBIDDEN_WORDS = {'soccer', 'religion', 'politics'}

texts = [
  'John likes soccer and politics',
  'The bitch was funny',  
]
for text in texts:
  intersection = FORBIDDEN_WORDS.intersection(set(text.lower().split()))

  if intersection:
      print('The text has at least one prohibited word', intersection)
  else:
      print('Text authorized:', text)
