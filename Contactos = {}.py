Contactos = {}
while True:  
    print("1 Agregar Contacto")
    print("2 Mostrar Contacto")
    print("3 Salir")
    Opcion = input("Elige una opcion:")
    if Opcion == "1":
            nombre = input("Escribe el nombre:")
            telefono = input("Escribe el telefono: ")
            Contactos[nombre]= telefono
    elif Opcion == "2":
            for nombre, teléfono in Contactos.items():
             print(nombre, ":", telefono)
    elif Opcion == "3":
     break 