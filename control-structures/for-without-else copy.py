FORBIDDEN_WORDS = ('soccer', 'religion', 'politics')

texts = [
  'John likes soccer and politics',
  'The bitch was funny',  
]
for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print('The text has at least one prohibited word', word)
            found = True
            break
    if not found:
        print('Text authorized:', text)
    
