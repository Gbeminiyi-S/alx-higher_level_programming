#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dictionary = dict(sorted(a_dictionary.items()))
    for key, value in new_dictionary.items():
        print(f"{key}: {value}")
