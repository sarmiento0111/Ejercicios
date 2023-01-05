# Determinante de una matriz cuadrada
import numpy as np
filas = int(input('ingrese el numero de filas de la matrix: '))
#columnas == filas
def crear_matriz(filas):
    f=-1
    c=-1
    e_fil=[]
    for i in range(0,filas):
        e_col =[]
        f +=1
        for j in range(0,filas):
            c +=1
            valor = int(input(f'Ingrese el valor del componente {i},{j}: '))
            e_col.append(valor)
        e_fil.append(e_col)
    return e_fil
matrizA=np.array(crear_matriz(filas))
# Matriz auxiliar
def subMatriz(mat, ren, col):
    copia = np.copy(mat)
    copia = np.delete(copia, (ren), axis=0)
    copia = np.delete(copia, (col), axis=1)
    return copia

def determinante(matrizA):
    if len(matrizA) == 2:
        return matrizA[0][0]*matrizA[1][1]-(matrizA[0][1]*matrizA[1][0])
    else:
        determ = 0.0
        for i in range(len(matrizA[0])):
            determ += ((-1)**i)*(matrizA[0][i])*determinante(subMatriz(matrizA,0,i))
    return determ


print(f"MatrizA= \n{matrizA} \n\nLa determiante de la matrizA es: \n{determinante(matrizA)}")
