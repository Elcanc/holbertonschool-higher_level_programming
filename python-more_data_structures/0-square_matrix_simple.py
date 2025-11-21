#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    l1 = matrix[0]
    l2 = matrix[1]
    l3 = matrix[2]
    matrix = [l1, l2, l3]
    e1 = l1[0]**2
    e2 = l1[1]**2
    e3 = l1[2]**2
    e4 = l2[0]**2
    e5 = l2[1]**2
    e6 = l2[2]**2
    e7 = l3[0]**2
    e8 = l3[1]**2
    e9 = l3[2]**2
    l11 = [e1, e2, e3]
    l22 = [e4, e5, e6]
    l33 = [e7, e8, e9]
    new_matrix = [l11, l22, l33]
    return new_matrix
