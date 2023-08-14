#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers in reverse of a list."""
    for n in reversed(range(len(my_list))):
        print("{:d}".format(my_list[n]))
