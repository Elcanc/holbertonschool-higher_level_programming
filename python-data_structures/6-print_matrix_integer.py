#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in range(len(a)):
            print("{}".format(a[b]))
    print('--')
