#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
	Finds the roots of a certain function with Newton's, bisection or secant method.
'''
from random import randint

'''
Calculates the derivative of a function using finite difference method.
'''
def derivative(f):
    def compute(x, dx):
        return (f(x+dx) - f(x))/dx
    return compute

'''
Finds the root a function using Newton's method.
'''
def findRootNewton(f, x, tolerance, maxIterations, dx=0.00000001):
	df = derivative(f)
	iterations = 1

	# Newton's method.
	while iterations < maxIterations:
		x1 = x - f(x)/df(x, dx)
		t = abs(x1 - x)
		if t < tolerance:
			break
		x = x1
		iterations += 1
	return x

'''
Evaluates the function in x.
'''
def f(x, argument):
    return eval(argument)

'''
Obtains the argument of the function to evaluate.
'''
def obtainArgument():
	argument = ""
	testNumber = random.randint(0, 1000)
	while True:
		str_value = raw_input("f(x) = ")
		try:
			foo = f(testNumber, argument)
			argument = str_value
			break
		except:
			print("Invalid entry!")
	return argument

'''
Obtains the start point for finding the root.
'''
def obtainStartPoint():
	startPoint = 0.1
	while True:
		str_value = raw_input("Start point (default: 0.1) = ")
		if value == "":
			break
		else:
			try:
				startPoint = float(str_value)
				break
			except:
				print("Invalid entry!")
	return startPoint

'''
Obtains the required tolerance for finding the root.
'''
def obtainTolerance():
	tolerance = 0.00001
	while True:
		str_value = raw_input("Tolerance (default: 0.00001) = ")
		if value == "":
			break
		else:
			try:
				tolerance = float(str_value)
				break
			except:
				print("Invalid entry!")
	return tolerance

'''
Obtains the number of desired iterations to run.
'''
def obtainMaxIterations():
	maxIterations = 100000
	while True:
		str_value = raw_input("Number of iterations (default: 100000) = ")
		if value == "":
			break
		else:
			try:
				maxIterations = float(str_value)
				break
			except:
				print("Invalid entry!")
	return maxIterations

'''
Main method of the program.
'''
def main():
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

	# Definition of function.
	f = argument

	print("")

	try:
		if method == "N":
			root = findRootNewton(f, start, tolerance, maxIterations)
	except:
		print("Oops! Something went wrong.")
		print("Either the function is not continous or it doesn't have a root near the start point.")

	# Result.
	print("--> The closest root to " + str(start) + " is = " + str(root))
