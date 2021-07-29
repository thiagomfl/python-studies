import csv
from urllib import request


def readFile(url):
    with request.urlopen(url) as _input:
        print('Downloading CSV...')
        data = _input.read()
        print('Download Success!')

        for value in csv.reader(data.splitlines()):
            print(f'{value[8]}: {value[3]}')

if __name__ == '__main__':
    readFile(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
