def cache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())
        print(f"{func.__name__}{args}")

        if key in cache:
            print("Result was taken from cache")
            return print(cache[key])

        result = func(*args, **kwargs)
        cache[key] = result

        return print(result)

    return wrapper


@cache
def add_numbers(a, b):
    return a + b

add_numbers(1, 2)
add_numbers(2, 4)
add_numbers(1, 2)
