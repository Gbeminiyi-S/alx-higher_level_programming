#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) == list:
        for row in matrix:
            separator = ''
            for element in row:
                if separator != '':
                    print("{}".format(separator), end='')
                print("{:x}".format(element), end='')
                separator = ' '
            print("".format())
