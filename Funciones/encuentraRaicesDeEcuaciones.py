#!/usr/bin/python
# -*- encoding: utf-8 -*-

'''
Encuentra las raíces de una función dada por diversos métodos, como el de Newton, Biseccion y Secantes.
@author: Camilo Andrés Martínez M.
'''
import sympy
from sympy import *
from mpmath import findroot

'''
Créditos a daydreamer por esta función.
https://stackoverflow.com/questions/13733493/python-how-to-evaluate-a-function-which-is-string/13734176#13734176
'''
def definirFuncion(s):
	lhs, rhs = s.split("=", 1)
	rhs = rhs.rstrip('; ')
	args = sympy.sympify(lhs).args
	f = sympy.sympify(rhs)
	def f_func(*passed_args):
		argdict = dict(zip(args, passed_args))
		result = f.subs(argdict)
		return float(result)
		return f_func

'''
Obtiene el argumento de la función a evaluar.
'''
def obtenerArgumento():
	argumento = raw_input("f(x) = ")
	return argumento

'''
Obtiene el valor cercano a la raiz.
'''
def obtenerComienzo():
	comienzo = int(raw_input("Comienzo de la búsqueda = "))
	return comienzo

'''
Obtiene la tolerancia de la búsqueda de la raíz.
'''
def obtenerTolerancia():
	error = float(raw_input("Tolerancia de la raíz = "))
	return error

'''
Calcula las raíces de la función dada por argumento.
'''
def main():
	# try-except en caso que algún dato ingresado sea inválido.
	try:
		# Obtiene parámetros esenciales para la obtención de la raíz.
		argumento = obtenerArgumento()
		comienzo = obtenerComienzo()
		error = obtenerTolerancia()

		# Se define la función.
		f = definirFuncion("f(x) = " + argumento)

		print("")

		# Muestra la raíz de acuerdo a los parámetros.
		print("--> La raíz más cercana a " + str(comienzo) + " es = " + str(findroot(f, comienzo, solver='secant', tol=error, verify=False)))
	except:
		print("Función inválida!")
