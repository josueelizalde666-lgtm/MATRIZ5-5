## Programa sencillo para realizar una reserva en el cine

# Matriz de 3 filas por 4 columnas, todos los asientos están libres
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar la ubicación del asiento que se desea reservar
fila = int(input("Digite la fila (0 a 2): "))
columna = int(input("Digite la columna (0 a 3): "))

# Cambiar el estado del asiento a reservado
asientos[fila][columna] = 1

print("\nSala de cine:")
print("0 = libre | 1 = reservado")

# Mostrar todos los asientos mediante dos bucles
for fila_actual in range(3):
    for columna_actual in range(4):
        print(asientos[fila_actual][columna_actual], end=" ")
    print()