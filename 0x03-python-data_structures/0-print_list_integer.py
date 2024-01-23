#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(max(len(tuple_a), len(tuple_b))):
        new_tuple += ((tuple_a[i] if i < len(tuple_a) else 0) +
                       (tuple_b[i] if i < len(tuple_b) else 0),)
    return new_tuple
