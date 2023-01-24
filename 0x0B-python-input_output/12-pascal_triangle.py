#!/usr/bin/python3
""" This module creates a function: pascal_triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s
    triangle of n """

    outer_list = []
    if n <= 0:
        return outer_list
    for i in range(n):
        inner_list = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                res = 1
            else:
                res = outer_list[i - 1][j - 1] + outer_list[i - 1][j]
            inner_list.append(res)
        outer_list.append(inner_list)
    return outer_list
