import inspect
import contextlib, io, time

def add_spaces(string, num_spaces=15):
    return (" " * num_spaces).join(string.splitlines(1))

def decorator_2(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*args, **kwargs)
        end = time.perf_counter()

        print(f'{func.__name__} call {wrapper.count} executed in {(end - start):.4f} sec')

        signature = inspect.signature(func)
        pad = 15
        print('Name: '.ljust(pad), func.__name__)
        print('Type: '.ljust(pad), type(func))
        print('Args: '.ljust(pad))
        print('positional: '.ljust(pad), add_spaces(f'{args}'))
        print('key-worded: '.ljust(pad), add_spaces(f'{kwargs}'))
        print('Signature: '.ljust(pad), add_spaces(str(signature)))
        print('Source: '.ljust(pad), add_spaces(inspect.getsource(func)))
        print('Output: '.ljust(pad), add_spaces(f.getvalue()))

    wrapper.count = 0
    return wrapper
