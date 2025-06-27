#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row_idx in matrix:
        new_matrix_sq = map(lambda num: num ** 2, row_idx)
        new_matrix_list = list(new_matrix_sq)
        new_matrix.append(new_matrix_list)
    return (new_matrix)
