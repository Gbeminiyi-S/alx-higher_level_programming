#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == biggest:
                return key
    else:
        return None
