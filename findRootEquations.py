#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Finds the roots of a certain function with Newton's, bisection or secant method.
'''
from random import randint

def findRootNewton(argument, startPoint, tolerance, maxIterations):
	"""	Finds the root a function using Newton's method """
	dx = 0.00000001
	x = startPoint
	iterations = 1

	# Newton's method.
	while iterations < maxIterations:
		df = (f(x+dx, argument) - f(x, argument))/dx # Derivative of the function in x.
		x1 = x - f(x, argument)/df
		t = abs(x1 - x)
		if t < tolerance:
			break
		x = x1
		iterations += 1
	return x

def f(x, argument):
	""" Evaluates the function in x """
	return float(eval(argument))

def obtainArgument():
	""" Obtains the argument of the function to evaluate """
	argument = ""
	testNumber = randint(0, 1000)
	while True:
		str_value = raw_input("f(x) = ")
		try:
			foo = f(testNumber, str_value)
			argument = str_value
			break
		except:
			print("Invalid entry!")
	return argument

def obtainStartPoint():
	""" Obtains the start point for finding the root """
	startPoint = 0.1
	while True:
		str_value = raw_input("Start point (default: 0.1) = ")
		if str_value == "":
			break
		else:
			try:
				startPoint = float(str_value)
				break
			except:
				print("Invalid entry!")
	return startPoint

def obtainTolerance():
	""" Obtains the required tolerance for finding the root """
	tolerance = 0.00001
	while True:
		str_value = raw_input("Tolerance (default: 0.00001) = ")
		if str_value == "":
			break
		else:
			try:
				tolerance = float(str_value)
				break
			except:
				print("Invalid entry!")
	return tolerance

def obtainMaxIterations():
	""" Obtains the number of desired iterations to run """
	maxIterations = 100000
	while True:
		str_value = raw_input("Number of iterations (default: 100000) = ")
		if str_value == "":
			break
		else:
			try:
				maxIterations = float(str_value)
				break
			except:
				print("Invalid entry!")
	return maxIterations

def main():
	""" Main method """
	# Definition of essential parameters.
	method = "N"
	while True:
		str_value = raw_input("Method [N: Newton (default), S: Secant, B: Bisection]: ")
		if str_value == "":
			break

		if str_value != "N" and str_value != "S" and str_value != "B":
			print("Invalid entry!")
		else:
			method = str_value
			break

	argument = obtainArgument()
	start = obtainStartPoint()
	error = obtainTolerance()
	maxIterations = obtainMaxIterations()

	print("")

	try:
		if method == "N":
			root = findRootNewton(argument, start, error, maxIterations)

		# Result.
		print("--> The closest root to " + str(start) + " is = " + str(root))
	except:
		print("Oops! Something went wrong.")
		print("Either the function is not continous or it doesn't have a root near the start point.")
