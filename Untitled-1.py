# crear una matriz vacia de 5 filas y 5 colucnas
matriz = [[0 for _ in range(5)] for _ in range(5)]

# recorrer la mtriz para pedir los valores al usuario
for i in range(5):
    for j in range(5):
        valor = int(input(f"ingrese el valor para la posición[{i}][{j}]: "))
        matriz[i][j] = valor

# mostrar la matriz ingresadaa
print("\nmatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()    