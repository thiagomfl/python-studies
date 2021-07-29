def fibonacci(limit):
    result = [0, 1]

    while result[-1] < limit:
        result.append(sum(result[-2:]))

    return result

    
if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
