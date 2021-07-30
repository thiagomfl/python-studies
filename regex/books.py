import re

titles = [
    "Babycakes (1984)",
    "Sure of You (1989)",
    "Tales of the City (1978)",
    "Mary Ann in Autumn (2010)",
    "Significant Others (1987)",
    "Michael Tolliver Lives (2007)",
    "More Tales of the City (1980)",
    "Further Tales of the City (1982)",
    "The Days of Anna Madrigal (2014)",
]
titles.sort()

fixed_titles = []

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')

for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)
    fixed_titles.append(result)

fixed_titles.sort()

print(fixed_titles)
