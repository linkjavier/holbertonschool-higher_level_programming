#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = [None] * len(my_list)
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        for i in range(0, len(my_list)):
            new[i] = my_list[i]
        new[idx] = element
        return new
