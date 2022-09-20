from task3 import Decorator_1, Decorator_2
from datetime import datetime


class Decorator_2_1(Decorator_1):
    def __init__(self, func):
        super(Decorator_2_1, self).__init__(func)

    def __call__(self, *args, **kwargs):
        try:
            func_res = super(Decorator_2_1, self).__call__(*args, **kwargs)
            return func_res
        except Exception as err:
            with open("error_logs.txt", "a+") as f:
                f.write(f"\nError: {str(err)}")
                timestamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
                f.write(f", Timestamp: {timestamp}")


class Decorator_2_2(Decorator_2):
    def __init__(self, func):
        super(Decorator_2_2, self).__init__(func)

    def __call__(self, *args, **kwargs):
        try:
            func_res = super(Decorator_2_2, self).__call__(*args, **kwargs)
            return func_res
        except Exception as err:
            with open("error_logs.txt", "a+") as f:
                f.write(f"\nError: {str(err)}")
                timestamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
                f.write(f", Timestamp: {timestamp}")
