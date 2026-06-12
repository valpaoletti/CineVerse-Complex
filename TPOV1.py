import random


def ordenar_las_peliculas(matriz):
    '''
    ordenar_las_peliculas
    [Esta funcion ordena la lista de peliculas, poniendo primero las mas vendidas. Si dos peliculas tienen la misma cantidad de entradas vendidas, las ordena por nombre de forma alfabetica]
    Hecha por: Axel Rodriguez
    '''
    for i in range(0,len(matriz)-1):
        for c in range(i+1,len(matriz)):

            if matriz[i][4] < matriz[c][4]:
                #En esta caso se ordena por cantidad de entradas vendidas
                aux = matriz[i]
                matriz[i] = matriz[c]
                matriz[c] = aux

            elif matriz[i][4] == matriz[c][4]:
                
                #En este caso ambas peliculas tienen la misma cantidad de entradas vendidas, se organiza alfabéticamente
                if matriz[i][0] > matriz[c][0]:
                    aux = matriz[i]
                    matriz[i] = matriz[c]
                    matriz[c] = aux
    return matriz


def darle_formato_a_los_Strings(cadena):
    '''
    [darle_formato_a_los_strings]
    Esta función sirve para acomodar el texto que escribe el usuario. Le saca los espacios que sobran al principio y al final y convierte todo a minúsculas, para que sea más fácil encontrar una película aunque el usuario la escriba de distintas maneras.
    Hecha por: Veleria Paoletti
    '''
    cadena_sin_espacio = cadena.strip()
    cadena_minuscula = cadena_sin_espacio.lower()

    return cadena_minuscula


def alta_peliculas(matriz):
    '''
    alta_peliculas(matriz)
    Esta función busca que se ingresen películas y que, a medida que eso ocurra, se vayan agregando a la matriz.
    Ejemplo de como quedaría:

    matriz = [

        ["Avatar","Ciencia Ficcion",160,14,25,1000.0,"En cartelera"],
        ["Auperman","Accion",120,12,35,2000.0,"Finalizada"]

    ]
    Hecha por: Oriana Herrera
    '''
    #Definimos listas
    lista_genero = ["Acción","Aventura","Comedia","Drama","Ciencia Ficción","Terror","Animación", "Documental"]
    lista_estados = ["En cartelera","Próximo estreno","Función especial","Finalizada"]
    lista_letras_aleatorias = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    

    print("\n----------------------\nALTA DE PELICULAS\n----------------------\n")
    datos = int(input("Los datos:\n[1] Van a ingresarse por teclado.\n[2] Van a generarse automáticamente (versión para pruebas).\nSu respuesta: "))
    while datos != 1 and datos != 2:
        datos = int(input("El valor ingresado es inválido.\n [1] Datos ingresados por teclado.\n[2] Versión para pruebas.\nSu respuesta: "))
    
    if datos == 1:
        respuesta = "si" #empezamos con un si ya definido para que entre directo al ciclo while
        
        while respuesta == "si":
            
            print("\n----------------------\nALTA DE PELICULAS\n----------------------\n")

            lista_datos_de_la_pelicula = []
            
            #Nombre de la pelicula
            nombre_pelicula = input("Ingrese el nombre de la pelicula: ").title()
            while nombre_pelicula == "":
                nombre_pelicula = str(input("Por favor, ingrese el nombre de la pelicula: ")).title()
            lista_datos_de_la_pelicula.append(nombre_pelicula)

            #Generos
            print("\nGeneros disponibles: [1] Acción. [2] Aventura. [3] Comedia. [4] Drama. [5] Ciencia Ficción. [6] Terror. [7] Animación. [8] Documental.")
            genero = int(input("Ingrese el género de la película: "))
            while genero >= 9 or genero < 1:

                print("\n¡Valor fuera de rango, género incorrecto!")
                print("\nGeneros disponibles: [1] Acción. [2] Aventura. [3] Comedia. [4] Drama. [5] Ciencia Ficción. [6] Terror. [7] Animación. [8] Documental.")
                genero = int(input("Ingrese el género de la película: "))

            nombre_del_genero = lista_genero[genero-1] #la ubicación del género dentro de la lista siempre va a ser una unidad mas chica
            lista_datos_de_la_pelicula.append(nombre_del_genero)

            #Duración
            duracion_pelicula = int(input("\nIngrese la duración de la pelicula (en minutos): "))
            while duracion_pelicula <= 0:
                duracion_pelicula=int(input("Duración inválida, intente de nuevo.\nIngrese la duración de la pelicula (en minutos): "))
            lista_datos_de_la_pelicula.append(duracion_pelicula)

            #Sala
            sala = int(input("\nIngrese el número de la sala: "))
            while sala <= 0:
                sala = int(input("El número de sala es inválido, intente de nuevo.\n Número de sala: "))
            lista_datos_de_la_pelicula.append(sala)

            #Entradas
            cantidad_entradas = int(input("\nIngrese la cantidad de entradas vendidas: "))
            while cantidad_entradas < 0:
                cantidad_entradas = int(input("La cantidad de entradas es inválida, intente de nuevo.\nCantidad de entradas: "))
            lista_datos_de_la_pelicula.append(cantidad_entradas)

            #Precio
            precio_promedio = float(input("\nIngrese el precio de la entrada: "))
            while precio_promedio < 0:
                precio_promedio = float(input("El valor de las entradas es inválido, intente de nuevo.\n Precio de la entrada: "))
            lista_datos_de_la_pelicula.append(precio_promedio)

            #Estados
            print("\nEstados posibles: [1] En cartelera. [2] Próximo estreno. [3] Función especial. [4] Finalizada.")
            opcion = int(input("Ingrese el estado de la cartelera: "))
            while opcion > 4 or opcion < 1:

                print("\nDicha opción no existe, intente de nuevo :D")
                print("\nEstados posibles: [1] En cartelera. [2] Próximo estreno. [3] Función especial. [4] Finalizada.")
                opcion = int(input("Ingrese el estado de la cartelera: "))

            texto_estado = lista_estados[opcion-1] #la ubicación del estado dentro de la lista siempre va a ser una unidad mas chica
            lista_datos_de_la_pelicula.append(texto_estado)
            
            #Agregar a la matriz
            matriz.append(lista_datos_de_la_pelicula)

            #Definir continuidad del ciclo while
            respuesta = str(input("\n¿Va a seguir ingresando películas? (respuesta por si o por no): ")).lower()
            while respuesta != "si" and respuesta != "no":
                respuesta = str(input("Respuesta inválida.\n¿Va a seguir ingresando películas? (respuesta por si o por no): ")).lower()
    
    elif datos == 2:
        respuesta = "si" #empezamos con un si ya definido para que entre directo al ciclo while
        
        while respuesta == "si":
            print("\n----------------------\nALTA DE PELICULAS\n----------------------\n-Versión Pruebas\n")

            lista_datos_de_la_pelicula = []

            #Nombre de la pelicula
            nombre_pelicula = random.choice(lista_letras_aleatorias)
            print("Nombre: ",nombre_pelicula,".")
            lista_datos_de_la_pelicula.append(nombre_pelicula)

            #Géneros
            genero = random.randint(0,7)
            nombre_del_genero = lista_genero[genero]
            print("Género: ",nombre_del_genero,".")
            lista_datos_de_la_pelicula.append(nombre_del_genero)

            #Duración
            duracion_pelicula = random.randint(1,240)
            print("Nota: se estableció un límite máximo de 4 horas (240 minutos) para pruebas.\nDuración: ",duracion_pelicula,"minutos.")
            lista_datos_de_la_pelicula.append(duracion_pelicula)
            
            #Sala
            sala = random.randint(1,100)
            print("Nota: se estableció un límite máximo de 100 salas para pruebas.\nSala: ",sala,".")
            lista_datos_de_la_pelicula.append(sala)

            #Entradas
            cantidad_entradas = random.randint(0,350)
            print("Nota: se estableció un límite máximo de 350 butacas para pruebas.\nEntradas: ",cantidad_entradas,".")
            lista_datos_de_la_pelicula.append(cantidad_entradas)

            #Precio
            precio_promedio = random.randint(1,30000)
            print("Nota: se estableció un límite máximo de $30000 de para pruebas.\nPrecio: $",precio_promedio,".")
            lista_datos_de_la_pelicula.append(precio_promedio)

            #Estados
            estado = random.randint(0,3) 
            texto_estado = lista_estados[estado]
            print("Estado: ",texto_estado,".")
            lista_datos_de_la_pelicula.append(texto_estado)
            
            #Agregar a la matriz
            matriz.append(lista_datos_de_la_pelicula)

            respuesta = str(input("\n¿Va a seguir generando valores aleatorios? (respuesta por si o por no): ")).lower()
            while respuesta != "si" and respuesta != "no":
                respuesta = str(input("Respuesta inválida.\n¿Va a seguir generando valores aleatorios? (respuesta por si o por no): ")).lower()
            
    return matriz


def baja_peliculas(matriz):
    '''
    [baja_peliculas]
    Esta función permite eliminar una película del catálogo. Primero muestra todas las películas registradas, luego pide el nombre de la película que se quiere borrar, la busca en la lista y, si existe y está marcada como "Finalizada", pide una confirmación antes de eliminarla. Esto evita que se borren películas por error o que se eliminen películas que todavía siguen en cartelera.
    Hecha por: Valeria Paoletti
    '''
    
    print("Títulos:")
    for i in range(0,len(matriz)):
        print(f" Nombre:{matriz[i][0].title()}  Género: {matriz[i][1]}. Duración: {matriz[i][2]}. Sala: {matriz[i][3]}. Cantidad de entradas: {matriz[i][4]}. Precio promedio: {matriz[i][5]}. Estado: {matriz[i][6]}.")


    nombre_de_la_pelicula_input = input("Ingrese el nombre de la película: ")
    while nombre_de_la_pelicula_input == "":
       nombre_de_la_pelicula_input = input("Por favor, ingrese el nombre de la película: ")
    
    nombre_de_la_pelicula = darle_formato_a_los_Strings(nombre_de_la_pelicula_input)

    posicion_de_pelicula_a_eliminar = busqueda_de_la_pelicula(matriz,nombre_de_la_pelicula)

    


    if posicion_de_pelicula_a_eliminar != -1:
        
       

        if matriz[posicion_de_pelicula_a_eliminar][6] == "Finalizada":
            

       

            print("¿SEGURO QUE QUIERE ELIMINAR ESTA PELICULA?")

            confirmar = int(input("Ingrese [1] si quiere eliminar la película o [2] cancelar operación: "))

            while confirmar != 1 and confirmar != 2:
                print("Ingrese una opción válida.")
                
                confirmar = int(input("Ingrese [1] si quiere eliminar la película o [2] cancelar operación: "))
                


            if confirmar == 1:
                
                matriz.pop(posicion_de_pelicula_a_eliminar)
                print("¡La película se eliminó exitosamente!")

            
            else:

                print("¡La operación se canceló!")

        
        else:

            print("¡La pelicula no esta finalizada!")
   
    else:

        print("La película ingresada no está en el catálogo.")
    return matriz

def busqueda_de_la_pelicula(matriz,nombre_de_la_pelicula):
    '''
    [sta función se encarga de buscar una película dentro de la lista. Recorre todas las películas registradas y compara sus nombres con el que ingresó el usuario. Si la encuentra, devuelve la posición donde está guardada; si no la encuentra, devuelve -1 para indicar que la película no existe en el catálogo.n]
    Hecha por: Emma Mealla
    '''
    pos = -1

    for i in range(0,len(matriz)):

        if matriz[i][0] == nombre_de_la_pelicula:

            pos = i
    
    return pos


def modificar_peliculas(matriz):
    '''
    [Esta función permite actualizar los datos de una película ya registrada. Primero busca la película que el usuario quiere modificar y, si la encuentra, ofrece la posibilidad de cambiar cada uno de sus datos (nombre, género, duración, sala, entradas, precio y estado). También permite dejar un dato sin cambios si así se desea.]
    Hecha por: Emma Mealla
    '''
    #imprimir los titulos
    print("Títulos:")
    for i in range(0,len(matriz)):

        print(matriz[i][0]) 

    titulo_de_la_pelicula_a_modificar = input("Ingrese el nombre de la película a modificar: ")
    while titulo_de_la_pelicula_a_modificar == "":
       titulo_de_la_pelicula_a_modificar = input("Por favor, ingrese el nombre de la película a modificar: ")
    
    posicion_de_la_pelicula = busqueda_de_la_pelicula(matriz,titulo_de_la_pelicula_a_modificar)

    if posicion_de_la_pelicula != -1:
        
        lista_genero = ["Acción","Aventura","Comedia","Drama","Ciencia Ficción","Terror","Animación", "Documental"]

        lista_estados = ["En cartelera","Próximo estreno","Función especial","Finalizada"]
       
        nombre_de_la_pelicula = input("Ingrese el nuevo nombre de la pelicula o ingrese un -1 para para no cambiar este atributo: ")

        while titulo_de_la_pelicula_a_modificar == "":
           titulo_de_la_pelicula_a_modificar = input("Por favor, ingrese el nombre de la película a modificar: ")
        

        print("Generos disponibles: [1] Acción. [2] Aventura. [3] Comedia. [4] Drama. [5] Ciencia Ficción. [6] Terror. [7] Animación. [8] Documental.")

        genero = int(input("Ingrese el genero de la pelicula o ingrese un -1 para para no cambiar este atributo: "))

        while (genero >= 9 or genero < 1) and genero != -1:

            print("El género ingresado es incorrecto!")
            print("Generos disponibles: [1] Acción. [2] Aventura. [3] Comedia. [4] Drama. [5] Ciencia Ficción. [6] Terror. [7] Animación. [8] Documental.")
            genero = int(input("Ingrese el género de la película: "))

        if genero != -1:
            texto_del_genero = lista_genero[genero-1]



        duracion_pelicula = int(input("Ingrese la duración de la película o ingrese un -1 para para no cambiar este atributo: "))

        sala = int(input("Ingrese el número de la sala o ingrese un -1 para para no cambiar este atributo: "))
        while sala <= 0 and sala != -1:
            sala = int(input("¡El valor ingresado es inválido! Por favor, ingrese el número de la sala o ingrese un -1 para para no cambiar este atributo: "))
        
        cantidad_entradas = int(input("Ingrese la cantidad de entradas vendidas o ingrese un -1 para para no cambiar este atributo: "))
        while cantidad_entradas <= 0 and cantidad_entradas != -1:
            cantidad_entradas = int(input("¡El valor ingresado es inválido! Por favor, ngrese la cantidad de entradas vendidas o ingrese un -1 para para no cambiar este atributo: "))
        
        precio_promedio = float(input("Ingrese el precio de la entrada o ingrese un -1.0 para para no cambiar este atributo: "))
        while precio_promedio <= 0 and precio_promedio != -1:
            precio_promedio = float(input("¡El valor ingresado es inválido! Por favor, ingrese el precio de la entrada o ingrese un -1.0 para para no cambiar este atributo: "))
        
        print("Estados posibles: [1] En cartelera. [2] Próximo estreno. [3] Función especial. [4] Finalizada.")
        opcion = int(input("Ingrese el estado de la cartelera o ingrese un -1 para para no cambiar este atributo: "))

        while (opcion > 4 or opcion < 1) and opcion != -1:

            print("¡Opción incorrecta!")
            print("Estados posibles: [1] En cartelera. [2] Próximo estreno. [3] Función especial. [4] Finalizada.")

            opcion = int(input("Ingrese el estado de la cartelera: "))

        if opcion != -1:
            texto_estado = lista_estados[opcion-1]

        if nombre_de_la_pelicula != "-1":
            matriz[posicion_de_la_pelicula][0] = nombre_de_la_pelicula

        if genero != -1:
            matriz[posicion_de_la_pelicula][1] = texto_del_genero
        
        if duracion_pelicula != -1:
            matriz[posicion_de_la_pelicula][2] = duracion_pelicula
        
        if sala != -1:
            matriz[posicion_de_la_pelicula][3] = sala
        
        if cantidad_entradas != -1:
            matriz[posicion_de_la_pelicula][4] = cantidad_entradas
        
        if precio_promedio != -1.0:

            matriz[posicion_de_la_pelicula][5] = precio_promedio

        if opcion != -1:
            matriz[posicion_de_la_pelicula][6] = texto_estado


        print("¡¡¡Se modificó la película con éxito!!!")


    else:
        print("La película ingresada no existe, ¡pruebe con otra!")
    return matriz
    
def informe(matriz):
    '''
    [Esta función genera un informe con todas las películas registradas. Antes de mostrarlas, las ordena según la cantidad de entradas vendidas, de mayor a menor. Si dos películas tienen la misma cantidad de ventas, las organiza alfabéticamente por nombre. Luego muestra toda la información de cada película de forma ordenada.]
    Hecha por: Axel Rodriguez
    '''
    matriz = ordenar_las_peliculas(matriz)
    for i in range(0,len(matriz)):

        print(f" Nombre:{matriz[i][0].title()}  Género: {matriz[i][1]}. Duración: {matriz[i][2]}. Sala: {matriz[i][3]}. Cantidad de entradas: {matriz[i][4]}. Precio promedio: {matriz[i][5]}. Estado: {matriz[i][6]}.")



def main():
    '''
    Menú principal de las funciones. Deriva en el resto de las funciones del programa
    Hecha por: Oriana Herrera
    '''

    matriz = []

    print("\nSISTEMA DE GESTIÓN: CINEVERSE COMPLEX\n")
    opcion = int(input("Elija una de las siguientes opciones:\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: "))
    
    while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
        print("Ingresó un valor incorrecto. Intente nuevamente.\n")
        opcion = int(input("Elija una de las siguientes opciones:\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: "))
    
    while opcion != 5:
        
        if opcion == 1:
            matriz = alta_peliculas(matriz)

        elif opcion == 2:
            matriz = baja_peliculas(matriz)

        elif opcion == 3:
            matriz = modificar_peliculas(matriz)

        elif opcion == 4:
            informe(matriz)


        print("\nSISTEMA DE GESTIÓN: CINEVERSE COMPLEX\n")
        opcion = int(input("Elija una de las siguientes opciones:\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: "))
        
        while opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
            print("Ingresó un valor incorrecto. Intente nuevamente.\n")
            opcion = int(input("Elija una de las siguientes opciones:\n[1] Registrar pelicula (Alta)\n[2] Eliminar pelicula (Baja)\n[3] Modificar de pelicula (Modificación)\n[4] Informe General\n[5] Salir\nSu respuesta: "))
    
    print("Grupo 2")

main()

