#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    temp1 = tuple_a + (0, 0)
    temp2 = tuple_b + (0, 0)
    tuple_c = temp1[0] + temp2[0], temp1[1] + temp2[1]
    return tuple_c
