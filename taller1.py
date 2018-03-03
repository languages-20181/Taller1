import networkx as nx 
import matplotlib.pyplot as plt

# print (" introduce un alfabeto,  separado por espacios: ")
# alf = list(map(str, sys.stdin.readline().strip().split(' ')))
# print (alf)

# print ("ingrese estados (separados por espacios): ")
# q = list(map(str,  sys.stdin.readline().strip().split(' ')))
# print (q)

# print (" introduce el estado inicial: ")
# q0= input()


# print (" estado final/es separados por espacios: ")
# qf = list(map(str,  sys.stdin.readline().strip().split(' ')))
# print (qf)

archivoEntrada = open("entrada.txt", 'r')
entradas = archivoEntrada.readlines()
alfabeto = entradas[0].strip().split(' ')
conjuntoEstados = entradas[1].strip().split(' ')
estadoInicial = entradas[2].strip()
estadosFinales = entradas[3].strip().split(' ')

# print (alfabeto)
# print(conjuntoEstados)
# print(estadoInicial)
# print(estadosFinales)

matrizTransicion={}

numeroRelaciones = len(conjuntoEstados) * len(alfabeto)
for i in range( 4, numeroRelaciones + 4):

    linea = entradas[i].strip().split(' ')
    estado1 = linea[0]
    estado2 = linea[1]
    simbolo = linea[2]

    if estado1 in matrizTransicion:
        matrizTransicion[estado1][simbolo] = estado2

    else:
        matrizTransicion[estado1] = {simbolo:estado2}

print(matrizTransicion)

while 1:
    print ("\n ingrese cadena a evaluar por el automata")

    cadenaEntrada= input ()

    estadoActual = estadoInicial

    for i in cadenaEntrada:
        estadoActual = matrizTransicion[estadoActual][i]

    if estadoActual in estadosFinales:
        print (" cadena aceptada, MUY BIEN! ")
    else:
        print (" cadena no aceptada ")

    print("")
    print("desea evaluar otra cadena (y/n)")
    respuesta = input()
    if respuesta == "y":
        continue
    else:
        break
