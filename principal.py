#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath("E:/Aplicaciones/Proyectos/University-problems-solvers/Funciones"))

import introduccion
import centrarFrase
import multiplicarMatrices
import encuentraRaicesDeEcuaciones
import encuentraDeterminanteMatriz

'''
	Función principal del programa.
'''
def main():
    introduccion.mostrarTexto()

    # Loop que ejecuta la opción ingresada y se devuelve.
    while True:
        # Loop que se asegura que la opción ingresada exista.
        while True:
            opcion = introduccion.tomarOpcion()

            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 99 or opcion == 100:
                break
            else:
                print ('*' + centrarFrase.main('Opción inválida', 0 ) + '*')

        print ("")

        # Condiciones para la ejecución de las opciones.
        if opcion == 1:
            encuentraRaicesDeEcuaciones.main()
        elif opcion == 2:
            encuentraDeterminanteMatriz.main()
        elif opcion == 3:
            multiplicarMatrices.main()
        elif opcion == 99:
            introduccion.mostrarOpciones()
        elif opcion == 100:
            exit()

        print ("")

'''
	Ejecuta el programa.
'''
if __name__ == "__main__":
    main()
