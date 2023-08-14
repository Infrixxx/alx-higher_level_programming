#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""
    for a in matrix:
        for b in a:
            if b != 0:
                print(" ", end='')
            print("{:d}".format(b), end='')
        print()
