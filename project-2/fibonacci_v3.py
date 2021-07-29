def fibonacci(limit):
    penultimate = 0
    last = 1

    print(f'{penultimate},{last}', end=',')

    while last < limit:
        penultimate, last = last, penultimate + last
        
        print(last, end=',')

    
if __name__ == '__main__':
    fibonacci(1000)
