import inspect
import contextlib, io, time
from task2 import add_spaces
from datetime import datetime

### Test both the class decorator and function decorator ?????????????
time_exec = {}

def rank_exec():
    global time_exec
    return dict(sorted(time_exec.items(), key=lambda x: x[1]))

def plot_rank_exec():
    ranked_dict = rank_exec()

    print('PROGRAM'.ljust(20), '|', 'RANK'.ljust(20), '|', 'TIME ELAPSED'.ljust(20))
    for i, (key, value) in enumerate(ranked_dict.items()):
        print(str(key).ljust(22), str(i + 1).ljust(22), str(value).ljust(22))

class Decorator_4:
    def __init__(self, func):
        self.num_calls = 0
        self.func = func
        self.func_name = func.__name__

    def __call__(self, *args, **kwargs):
        global time_exec
        self.num_calls += 1

        try:
            start = time.perf_counter()
            with contextlib.redirect_stdout(io.StringIO()) as f_cont:
                self.func(*args, **kwargs)
            end = time.perf_counter()

            signature = inspect.signature(self.func)
            pad = 15
            with open(f"./exec_info/{self.func.__name__}.txt", 'w' if self.num_calls == 1 else 'a') as f:
                f.write(f'{self.func.__name__} call {self.num_calls} executed in {(end - start):.4f} sec' + '\n')
                f.write('Name: '.ljust(pad) + self.func.__name__ + '\n')
                f.write('Type: '.ljust(pad) + str(type(self.func)) + '\n')
                f.write('Args: '.ljust(pad) + '\n')
                f.write('positional: '.ljust(pad) + add_spaces(f'{args}') + '\n')
                f.write('key-worded: '.ljust(pad) + add_spaces(f'{kwargs}') + '\n')
                f.write('Signature: '.ljust(pad) + add_spaces(str(signature)) + '\n')
                f.write('Source: '.ljust(pad) + add_spaces(inspect.getsource(self.func)) + '\n')
                f.write('Output: '.ljust(pad) + add_spaces(f_cont.getvalue()) + '\n')

            time_exec[self.func_name] = (end - start)
        except Exception as err:
            with open(f"./error_logs/{self.func.__name__}", 'w') as f:
                f.write(f'Error: {str(err)}')
                timestamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
                f.write(f', Timestamp: {timestamp}')


