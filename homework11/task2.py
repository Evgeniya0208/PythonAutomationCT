def log(log_level, output_file):
    def decorator_log(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            log_message = f"{log_level} : Function {func.__name__} was called with arguments {args}\n"
            try:
                with open(output_file, 'a') as output:
                    output.write(log_message)
            except Exception as e:
                print("There is a Problem", str(e))
        return wrapper
    return decorator_log


@log('function log', 'output.txt')
def add_numbers(a, b):
    return a + b

add_numbers(1, 2)
add_numbers(2, 4)
add_numbers(3, 4)