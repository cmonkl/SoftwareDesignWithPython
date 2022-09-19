import time, io
import contextlib

def decorator_1(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func_res = func(*args, **kwargs)
        end = time.perf_counter()

        wrapper.func_output = f.getvalue()

        print(f'{func.__name__} call {wrapper.count} executed in {(end-start):.4f} sec')
        return func_res

    wrapper.count = 0
    wrapper.func_output = None
    return wrapper
