#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Multiplies 2 matrices given by the user.
'''
import obtainUnsquareMatrix
import printMatrix

def main():
	""" Main method """
	print ("First matrix:")
	print ("")
	matrixA = obtainUnsquareMatrix.main()

	print ("Second matrix:")
	print ("")
	matrixB = obtainUnsquareMatrix.main()

	print ("")
	print ("The result is: ")
	print ("")

	printMatrix.main(matrixA)
