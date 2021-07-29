def fibonacci(qty, sequence=(0, 1)):
    return sequence if len(sequence) == qty else \
    fibonacci(qty, sequence + (sum(sequence[-2:]), ))

    
if __name__ == '__main__':
    for fib in fibonacci(30):
        print(fib)
