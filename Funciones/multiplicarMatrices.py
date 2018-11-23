#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import numpy
import obtenerMatricesnxm
import mostrarMatriz

'''
	Multiplica las matrices ingresadas.
'''
def main():
    # Obtiene las matrices a multiplicar.
    matrices = obtenerMatricesnxm.main()

    print ("El resultado de la multiplicación es:")

    # Multiplica las matrices.
    matrizResultado = numpy.linalg.multi_dot(matrices)

    # Muestra la matriz.
    mostrarMatriz.main(matrizResultado)
