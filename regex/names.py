import re


def parse_name(string):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(string)
	
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))


if __name__ == '__main__':
	parse_name("Mrs. Tilda Swinton")
