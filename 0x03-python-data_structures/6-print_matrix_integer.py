#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""
    for a in range(len(matrix)):    #from 0 to length of elements in list
        for b in range(len(matrix[a])):    #from 0 to lenght of elements in sub list
            if b == 2:
                print("{:d}".format(matrix[a][b]), end='')  #creates space after printing element
            print("{:d}".format(matrix[a][b]), end=' ')    #removes space for last element
        print() #creates newline
