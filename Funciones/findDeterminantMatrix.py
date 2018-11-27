#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import obtainSquareMatrix

'''
	Finds the determinant of a matrix.
'''

def minor(matrix, i):
	""" Finds the minor of a matrix given a row i. """
    n = len(matrix)
    minor = []
    minor = matrix.copy()
    row = i//n
    col = i%n - 1
    del minor[row] # Deletes the first row
    for j in list(range(len(minor))): # Deletes column i
        recover_row = list(matrix[j])
        del minor[j][col]
        matrix[j] = recover_row
    return minor

def det(A):
    """ Recursive function to find determinant """
    if len(A) == 1:
        return A[0][0]
    else:
        determinant = 0
        for x in list(range(len(A))): # Iterates along first row finding cofactors
            determinant += A[0][x] * (-1)**(2 + x) * det(minor(A, x)) # Adds successive elements times their cofactors

        return determinant

def main():
	""" Main function """
    matrix = obtainSquareMatrix.main()
    print ("")

    # In case an error occured obtaining the matrix.
    if matrix is not None:
        print ("The determinant is = " + det(matrix))
