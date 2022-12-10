#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        total = 0
        count = 0
        for element in my_list:
            i, j = element
            total += (i * j)
            count += j
        return total / count
