import random
from task1 import decorator_1
from task2 import decorator_2
from task3 import Decorator_3, time_exec, plot_rank_exec
from task4 import Decorator_4
import math

def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1]))

def find_arr_intersection(arr1, arr2):
    return list(filter(lambda x: x in arr1, arr2))

@Decorator_3
def pascal_triangle(n):
    last_row = [1]
    pad = n+4
    print('1'.center(pad))
    for i in range(n-1):
        row = [1]
        for j in range(i):
            row.append(last_row[j] + last_row[j+1])
        row.append(1)

        print(' '.join(map(str, row)).center(pad))
        last_row = row

@Decorator_4
def quadratic_equation_solver(a, b, c):
    if a != 0:
        d = b*b - 4*a*c

        if d > 0:
            x1 = -(b + math.sqrt(d)) / 2*a
            x2 = -(b - math.sqrt(d)) / 2*a
            return x1, x2
        elif d == 0:
            return -b / 2*a
        else:
            raise Exception('Not solvable in real numbers')

    elif b != 0:
        return -c / b
    else:
        raise Exception('Not solvable')


@Decorator_3
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(1, 751)
    for i in range(n):
        result += (i ** 2)


@Decorator_3
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


@Decorator_3
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


if __name__ == "__main__":
    print('task1')
    func()
    funx()
    func()
    funx()
    func()

    print('\ntask2')
    funh(None, bar2="")

    print('\ntask3')
    plot_rank_exec()

    print('\ntask4')
    quadratic_equation_solver(0, 0, 6)

    print(find_arr_intersection([1, 2, 3, 4, 5], [2, 3, 4]))
    pascal_triangle(5)