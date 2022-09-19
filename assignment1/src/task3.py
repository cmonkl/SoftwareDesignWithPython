import inspect
import contextlib, io, time
from task2 import add_spaces

time_exec = {}


def rank_exec():
    global time_exec
    return dict(sorted(time_exec.items(), key=lambda x: x[1]))


def plot_rank_exec():
    ranked_dict = rank_exec()

    pad = 20
    print("PROGRAM".ljust(pad), "|", "RANK".ljust(pad), "|", "TIME ELAPSED".ljust(pad))
    for i, (key, value) in enumerate(ranked_dict.items()):
        print(
            str(key).ljust(pad + 2),
            str(i + 1).ljust(pad + 2),
            str(value).ljust(pad + 2),
        )


class Decorator_1:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        self.func_output = None

    def __call__(self, *args, **kwargs):
        global time_exec
        self.num_calls += 1

        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func_res = self.func(*args, **kwargs)
            self.func_output = f.getvalue()
        end = time.perf_counter()

        with open("exec_info.txt", "a+") as f:
            f.write(
                f"{self.func.__name__} call {self.num_calls} executed in {(end - start):.4f} sec"
                + "\n"
            )

        time_exec[self.func.__name__] = end - start
        return func_res


class Decorator_2(Decorator_1):
    def __init__(self, func):
        super(Decorator_2, self).__init__(func)

    def __call__(self, *args, **kwargs):
        func_res = super(Decorator_2, self).__call__(*args, **kwargs)

        signature = inspect.signature(self.func)
        pad = 15

        with open("exec_info.txt", "a+") as f:
            f.write("Name: ".ljust(pad) + self.func.__name__ + "\n")
            f.write("Type: ".ljust(pad) + str(type(self.func)) + "\n")
            f.write("Sign: ".ljust(pad) + add_spaces(str(signature)) + "\n")
            f.write("Args: ".ljust(pad) + add_spaces(f"positional {args}") + "\n")
            f.write(" ".ljust(pad) + add_spaces(f"key-worded {kwargs} \n") + "\n")
            f.write(
                "Doc: ".ljust(pad - 4)
                + add_spaces(
                    self.func.__doc__[1:] if self.func.__doc__ is not None else "\n", 11
                )
            )
            f.write(
                "\nSource: ".ljust(pad)
                + add_spaces(inspect.getsource(self.func))
                + "\n"
            )
            f.write("Output: ".ljust(pad) + add_spaces(self.func_output) + "\n")

        return func_res
