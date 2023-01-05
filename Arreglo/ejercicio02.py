arreglo=[20, 15, 12, 11, 8, 4, 1]
arreglo.remove(1)
print(f"\nArreglo= {arreglo}")

suma = 0
cantidad_elementos = len(arreglo)
for valor in arreglo:
    suma = suma + valor
cantidad_elementos = len(arreglo)
promedio = suma / cantidad_elementos
print(f"\nEl promedio es {promedio}")