#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for s in range(len(i)):
            if s >= len(i) - 1:
                print("{:d}".format(i[s]), end='')
            else:
                print("{:d}".format(i[s]), end=' ')
        print("")
