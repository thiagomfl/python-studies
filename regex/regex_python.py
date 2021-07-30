import re

pattern = re.compile(r'^\(?\d{2}\)?\s?\d{5,}-?\d{4}$')
print(pattern)
print(type(pattern))

result = pattern.search('(81) 99811-3680')
print(result.group())