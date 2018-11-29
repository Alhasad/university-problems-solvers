#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Finds the determinant of a matrix.
'''
import obtainSquareMatrix

def det(matrix, mul):
	""" Recursive function to find the determinant of the given matrix """
	width = len(matrix)
	if width == 1:
		return mul * matrix[0][0]
	else:
		sign = -1
		total = 0
		for i in range(width):
			m = []
			for j in range(1, width):
				buff = []
				for k in range(width):
					if k != i:
						buff.append(matrix[j][k])
				m.append(buff)
			sign *= -1
			total += mul * det(m, sign * matrix[0][i])
		return total

def main():
	""" Main method """
	matrix = obtainSquareMatrix.main()
	print ("")

	# In case an error occured obtaining the matrix.
	if matrix is not None:
		print ("The determinant is = " + str(det(matrix, 1)))
