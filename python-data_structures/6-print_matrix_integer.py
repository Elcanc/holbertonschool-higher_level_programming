#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in range(len(a)):
            if i != a[-1]:
                print("{:d}".format(a[b]), end=' ')
            elif i == a[-1]:
                print("{:d}".format(a[b]), end='')
    print('--')
