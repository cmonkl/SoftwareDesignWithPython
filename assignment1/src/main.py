import random
from task1 import decorator_1
from task2 import decorator_2
from task3 import Decorator_2, Decorator_1, plot_rank_exec
from task4 import Decorator_2_1
import math


def sort_dict_by_value(dictionary):
    """
    Function to perform ascending sort of dictionary values

    :param dictionary: dictionary to be sorted
    """
    return dict(sorted(dictionary.items(), key=lambda x: x[1]))


def find_arr_intersection(arr1, arr2):
    """
    Function to find intersection of two lists

    :param arr1: first list
    :param arr2: second list
    """
    return list(filter(lambda x: x in arr1, arr2))


@Decorator_2
def pascal_triangle(n):
    """
    Function to print Pascal's triangle up to n lines

    :param n: number of lines
    """
    if n < 0:
        raise Exception("Number should be non negative")

    last_row = [1]
    pad = n + 4
    print("1".center(pad))
    for i in range(n - 1):
        row = [1]
        for j in range(i):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)

        print(" ".join(map(str, row)).center(pad))
        last_row = row


@Decorator_2_1
def quadratic_equation_solver(a, b, c):
    """
    Function to solve quadratic equation given by the coefficients:
    ax^2 + bx + c

    :param a: coefficient of the x**2
    :param b: coefficient of x
    :param c: free coefficient
    """
    if a != 0:
        d = b * b - 4 * a * c

        if d > 0:
            x1 = -(b + math.sqrt(d)) / 2 * a
            x2 = -(b - math.sqrt(d)) / 2 * a
            return x1, x2
        elif d == 0:
            return -b / 2 * a
        else:
            raise Exception("Not solvable in real numbers")

    elif b != 0:
        return -c / b
    else:
        raise Exception("Not solvable")


@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += i**2


@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float("-inf")
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


if __name__ == "__main__":
    print("task1")
    func()
    funx()
    func()
    funx()
    func()

    print("\ntask2")
    funh(None, bar2="")

    print("task3")
    d = {"three": 3, "four": 4, "one": 1, "two": 2}
    sort_dict_by_value(d)
    quadratic_equation_solver(2, 2, 3)
    find_arr_intersection([1, 2, 3], [2, 3, 5, 2])
    pascal_triangle(5)

    plot_rank_exec()

    print("\ntask4")
    quadratic_equation_solver(0, 0, 3)
