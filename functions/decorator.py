def log(fn):
    def decorator(*args, **kwargs):
        print(f'Start of function call: {fn.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

        result = fn(*args, **kwargs)
        print(f'Call result: {result}')
        return result
    return decorator


@log
def _sum(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(_sum(5, 2))
    print(sub(5, 2))
