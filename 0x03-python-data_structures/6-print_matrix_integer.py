#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        i = 0
        for integer in row:
            print("{:d}".format(integer), end="")
            if i != row_len-1:
                print(" ", end="")
            i = i+1
        print()
