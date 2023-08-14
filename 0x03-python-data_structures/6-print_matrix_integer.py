#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = ['{:d}'.format(column) for column in row]
        print(' '.join(formatted_row))
