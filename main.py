import funciones


def menu():
    '''
    Menú principal de las funciones. Deriva en el resto de las funciones del programa
    Hecha por: Oriana Nayla Herrera
    '''

    matriz = []

    funciones.guiones("SISTEMA DE GESTIÓN: CINEVERSE COMPLEX")
    opcion = input("Elija una de las siguientes opciones (números):\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: ")

    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
        if opcion.isdigit():
            opcion = int(opcion)

        if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
            print("Ingresó un valor incorrecto. Intente nuevamente.\n")
            opcion = input("Elija una de las siguientes opciones (números):\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: ")
        
    while opcion != 5:
        
        if opcion == 1:
            funciones.alta_peliculas(matriz)

        elif opcion == 2:
            funciones.baja_peliculas(matriz)

        elif opcion == 3:
            funciones.modificar_peliculas(matriz)

        elif opcion == 4:
            funciones.informe(matriz)


        funciones.guiones("SISTEMA DE GESTIÓN: CINEVERSE COMPLEX")
        opcion = input("Elija una de las siguientes opciones:\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: ")
        
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
            if opcion.isdigit():
                opcion = int(opcion)

            if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
                print("Ingresó un valor incorrecto. Intente nuevamente.\n")
                opcion = input("Elija una de las siguientes opciones (números):\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: ")
            
    print("Grupo 2")

menu()