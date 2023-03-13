import numpy as np

r1 = 2 
r2 = 2 
A=[]
b=[]

def num_ColyFilas(r1,r2):
    print( "Digite Numero de Columnas")
    r1 = input()
    print("Digite Numero de Filas")
    r1 = input()
    return r1,r2

def llenarmatriz(r1,r2,A):
    lista=[]
    
    for i in range(int(r1)):
        lista=[input("Digite el valor\n") for j in range(int(r2))]
        A.append(lista)
    print("<<<<<<<< Matriz >>>>>>>>")
    for i in A:
        print("[", end=" ")
        for j in i:
              print(j, end=" ")
        print("]")
    return A

def montante(A):
    # Convertir A a una matriz numpy
    A = np.array(A, dtype=float)

    # Obtener las dimensiones de la matriz A
    n = len(A)

    # Crear la matriz ampliada del sistema de ecuaciones
    M = A.copy()

    # Crear la matriz identidad
    I = np.identity(n)

    # Iterar sobre cada columna de la matriz M
    for j in range(n):
        # Iterar sobre cada fila debajo de la diagonal principal
        for i in range(j+1, n):
            # Dividir la fila i por el elemento diagonal correspondiente
            factor = M[i][j] / M[j][j]
            M[i] -= factor * M[j]
            I[i] -= factor * I[j]

    # Iterar sobre cada columna de la matriz M en orden inverso
    for j in range(n-1, -1, -1):
        # Dividir la fila j por el elemento diagonal correspondiente
        M[j] /= M[j][j]
        I[j] /= M[j][j]
        # Restar el múltiplo apropiado de la fila j de cada fila por encima de ella
        for i in range(j-1, -1, -1):
            factor = M[i][j]
            M[i] -= factor * M[j]
            I[i] -= factor * I[j]

    # Obtener el determinante de la matriz
    det = np.prod(np.diag(M))

    # Obtener la matriz inversa
    inv = I

    # Devolver la matriz resultante
    return det, inv, M

# Obtener el determinante, la matriz inversa y la solución de la matriz utilizando el método de Montante
print("Cambiar Num. de Filas y Columnas [Default 2x2] Y/N?")
resp1 = input().upper()
if resp1 == "Y":
  num_ColyFilas(r1,r2)

llenarmatriz(r1,r2,A)
det, inv, sol = montante(A)

# Imprimir los resultados
print("<<<<<<<< Determinante >>>>>>>>")
print(f"Determinante: {det}")
print("<<<<<<<< Matriz inversa >>>>>>>>")
print(f"Matriz inversa:\n{inv}")
print("<<<<<<<< Solución de la matriz >>>>>>>>")
print(f"Solución de la matriz:\n{sol}")




