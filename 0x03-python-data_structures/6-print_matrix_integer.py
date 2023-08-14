#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            print("{:d}".format(matrix[a][b]), end='')
            if b != len(matrix[a]) - 1:
                print(" ", end='')  # creates space after printing element (except for the last)
        print()  # creates newline
