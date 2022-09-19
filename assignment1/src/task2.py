import inspect
from task1 import decorator_1


def add_spaces(string, num_spaces=15):
    return (" " * num_spaces).join(string.splitlines(1))


def decorator_2(func):
    def wrapper(*args, **kwargs):
        dec_1 = decorator_1(func)
        func_res = dec_1(*args, **kwargs)

        signature = inspect.signature(func)
        pad = 14
        print("Name: ".ljust(pad), func.__name__)
        print("Type: ".ljust(pad), type(func))
        print("Sign: ".ljust(pad), add_spaces(str(signature)))
        print("Args: ".ljust(pad), add_spaces(f"positional {args}"))
        print(" ".ljust(pad), add_spaces(f"key-worded {kwargs} \n"))
        print(
            "Doc: ".ljust(pad - 4),
            add_spaces(func.__doc__[1:-1] if func.__doc__ is not None else "\n", 11),
        )
        print("Source: ".ljust(pad), add_spaces(inspect.getsource(func)))
        print("Output: ".ljust(pad), add_spaces(dec_1.func_output))
        return func_res

    return wrapper
