#!/usr/bin/python3
""" This module creates a function: pascal_triangle """


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s
    triangle of n """

    outer_list = []
    if n <= 0:
        return outer_list
    for line in range(n):
        inner_list = []
        for i in range(line + 1):
            res = 1
            if (i == 0) or (i == line):
                res = 1
            else:
                res = outer_list[line - 1][i - 1] + outer_list[line - 1][i]
            inner_list.append(res)
        outer_list.append(inner_list)
    return outer_list
