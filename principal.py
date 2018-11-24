#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath("E:/Aplicaciones/Proyectos/University-problems-solvers/Funciones"))

import introduction
import centerText
import findRootEquations

'''
	Main method of the whole app.
'''
def main():
    introduction.show()

    # Loop que ejecuta la opción ingresada y se devuelve.
    while True:
        # Loop que se asegura que la opción ingresada exista.
        while True:
            option = introduction.takeOption()

            if option == 1.1:
                break
            else:
                print ('*' + centerText.main('Invalid entry!', 0 ) + '*')

        print ("")

        # Condiciones para la ejecución de las optiones.
        if option == 1.1:
            findRootEquations.main()
        elif option == 100:
            exit()

        print ("")

'''
	Executes the app.
'''
if __name__ == "__main__":
    main()
