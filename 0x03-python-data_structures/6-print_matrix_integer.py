#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""
    for a in range(len(matrix)):    #from 0 to length of elements in list
        for b in range(len(matrix[a])):    #from 0 to lenght of elements in sub list
            if b != 3:
                print(" ", end='')  #creates space when it's not first element
            print("{:d}".format(matrix[a][b]), end='')
        print() #creates newline
