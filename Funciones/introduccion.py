#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import darAnchoDeConsola

'''
	Muestra las opciones disponibles.
'''
def mostrarOpciones():
    print ('1. Encontrar raíces de ecuaciones.')
    print ('2. Encontrar el determinante de una matriz nxn')
    print ('3. Multiplicar matrices.')
    print ('')
    print ('99. Mostrar las opciones de nuevo.')
    print ('100. Salir.')

'''
	Muestra la introducción completa.
'''
def mostrarTexto():
    titulo = 'Herramientras de universitario'
    anchoDeConsola = darAnchoDeConsola.main()

    print ('~' * anchoDeConsola)
    print (' ' * int(str((anchoDeConsola - len(titulo))//2)) + titulo + ' ' * int(str((anchoDeConsola - len(titulo))//2)))
    print ('~' * anchoDeConsola)
    print ('')
    mostrarOpciones()
    print ('')

'''
	Algoritmo que toma la opción del usuario.
'''
def tomarOpcion():
    anchoDeConsola = darAnchoDeConsola.main()

    print ('~' * anchoDeConsola)
    opcion = int(input("Opción: "))
    return opcion
