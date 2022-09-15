import time, io
import contextlib

def decorator_1(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*args, **kwargs)
        end = time.perf_counter()

        print(f'{func.__name__} call {wrapper.count} executed in {(end-start):.4f} sec')

    wrapper.count = 0
    return wrapper
