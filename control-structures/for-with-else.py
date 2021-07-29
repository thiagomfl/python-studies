FORBIDDEN_WORDS = ('soccer', 'religion', 'politics')

texts = [
  'John likes soccer and politics',
  'The bitch was funny',  
]
for text in texts:
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print('The text has at least one prohibited word', word)
            break
    else:
        print('Text authorized:', text)
