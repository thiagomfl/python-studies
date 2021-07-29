def fibonacci(qty):
    result = [0, 1]

    for _ in range(2, qty):
        result.append(sum(result[-2:]))

    return result

    
if __name__ == '__main__':
    for fib in fibonacci(30):
        print(fib)
