def fibonacci(qty):
    result = [0, 1]

    while True:
        result.append(sum(result[-2:]))

        if len(result) == qty:
            break

    return result

    
if __name__ == '__main__':
    for fib in fibonacci(30):
        print(fib)
