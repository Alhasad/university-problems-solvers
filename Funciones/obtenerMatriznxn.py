#!usr/bin/python
# -*- encoding: utf-8 -*-

'''
        Obtiene la matriz ingresada.
'''
def main():
    # try-except en caso que algún dato ingresado sea inválido o erróneo.
    try:
        n = int(raw_input("Dimensión de la matriz (ejemplo: 2 -> Da una matriz 2x2)= "))
        print ("")
        print ("Matriz " + str(n) + "x" + str(n) + ":")

        # Loop que crea las filas de la matriz como lista.
        i = 0
        matriz = []

        while i < n:
	    # Lista donde se guardará los datos de tipo "string".
            str_filaActual = []

	    # Ingreso de la fila en tipo "string".
            str_fila = raw_input("-> Fila " + str(i + 1) + ": ")

	    # Se dividen la cadena ingresada con los datos respecto a los espacios.
            str_filaActual = str_fila.split(" ")

	    # Se convierten los datos de tipo "string" en "float".
            filaActual = [float(x) for x in str_filaActual]

            if len(filaActual) == n:
                # Se añade la lista de número de la fila correspondiente a la matriz.
                matriz.append(filaActual)
                i += 1
            else:
                print ("El número de valores dados no coinciden con la dimensión de la matriz.")

        return matriz
    except:
	print ("")
        print ("Valor inválido!")

