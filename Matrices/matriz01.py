import numpy as np
filas = int(input('ingrese el numero de filas de la matrix: '))
columnas = int(input('ingrese el numero de columnas de la matriz: '))
def crear_matriz(filas,columnas):
    f=-1
    c=-1
    e_fil=[]
    for i in range(0,filas):
        e_col =[]
        f +=1
        for j in range(0,columnas):
            c +=1
            valor = int(input(f'Ingrese el valor del componente {i},{j}: '))
            e_col.append(valor)
        e_fil.append(e_col)
    return e_fil
matrizA=np.array(crear_matriz(filas,columnas))
matrizB=np.array(crear_matriz(filas,columnas))
print("Matriz A= \n",matrizA)
print("Matriz B= \n",matrizB)
suma=matrizA+matrizB
resta=matrizA-matrizB
multiplicacion=matrizA*matrizB
print(f"suma de matrices: \n{suma} \n\n resta de matrices: \n{resta} \n\n multiplicacion de las matrices: \n{multiplicacion}")