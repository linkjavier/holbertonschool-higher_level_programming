#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    custom = sorted(a_dictionary)
    for i in custom:
        print("{}: {}".format(i, a_dictionary[i]))
