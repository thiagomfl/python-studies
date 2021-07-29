def fibonacci(qty, sequence=(0, 1)):
    if len(sequence) == qty:
        return sequence
    
    return fibonacci(qty, sequence + (sum(sequence[-2:]), ))

    
if __name__ == '__main__':
    for fib in fibonacci(30):
        print(fib)
