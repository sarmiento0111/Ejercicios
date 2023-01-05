tamaño=int(input('tamaño del arreglo: '))
array1=[]
numero=int(input('ingrese un número para obtener los múltiplos: '))
for i in range(1,tamaño+1):
    aux=i*numero
    array1.append(aux)
print("\nArreglo= ",array1)