#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import numpy
import obtenerMatriznxn

'''
	Encuentra el determinante de la matriz proveída como parametro.
'''
def main():
    matriz = obtenerMatriznxn.main()
    print ("")

    # Condición, en caso que se haya obtenido un error al obtener la matriz.
    if matriz is not None:

        # Condición, en caso que la matriz ingresada sea un vector.
        if 1 < len(matriz):
            print ("El determinante es = " + str(numpy.linalg.det(matriz)))
        else:
            print ("La matriz ingresada es un vector.")
