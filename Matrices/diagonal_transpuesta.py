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

# Diagonal principal
diagonal_primaria=[]
for h in range(len(matrizA)):
    for k in range(len(matrizA)):
        numero2=matrizA[h][k]
        if [h]==[k]:
            diagonal_primaria.append(numero2)
# Matriz Transpuesta


print("\nMatriz A= \n",matrizA)
print(f"\nla diagonal principal de la matrizA es:\n{diagonal_primaria}")