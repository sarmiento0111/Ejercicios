tamaño=int(input('tamaño del arreglo: '))
array1=[]
array2=[]
for i in range(tamaño):
    array1.append(input('ingrese un nombre: '))
print("Array1= ",array1)
for x in range(tamaño):
    array2.append(len(array1[x]))
print("Array2= ",array2)