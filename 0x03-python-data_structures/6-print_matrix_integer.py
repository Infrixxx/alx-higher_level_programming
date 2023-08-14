#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for element in n:
            print("{:d}".format(element), end=" ")
        print()  # Move to the next line after printing each sublist
