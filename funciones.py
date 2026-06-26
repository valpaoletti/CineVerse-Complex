import random



def ordenar_las_peliculas(matriz):
    '''
    ordenar_las_peliculas
    [Esta funcion ordena la lista de peliculas, poniendo primero las mas vendidas. Si dos peliculas tienen la misma cantidad de entradas vendidas, las ordena por nombre de forma alfabética]
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



def darle_formato_a_los_Strings(cadena):
    '''
    [darle_formato_a_los_strings]
    Esta función sirve para acomodar el texto que escribe el usuario. Le saca los espacios que sobran al principio y al final y convierte todo a minúsculas, para que sea más fácil encontrar una película aunque el usuario la escriba de distintas maneras.
    Hecha por: Veleria Paoletti
    '''
    cadena_sin_espacio = cadena.strip()
    cadena_minuscula = cadena_sin_espacio.lower()

    return cadena_minuscula



def continuidad(mensaje):
    '''
    Esta función se utiliza en todas las funciones donde se le pide al usuario una confirmación por 'si' o por 'no' para continuar el ciclo while.
    La función incluye el ingreso por teclado de la confirmación (a la cual se la convierte en minúscula para que se adecúe a la condición del ciclo while) y la validación de la misma.
    Hecha por: Oriana Nayla Herrera
    '''
    opcion = input(mensaje).lower()
    while opcion != "si" and opcion != "no":
        print("El valor ingresado no es válido, intentelo nuevamente. ",end="")
        opcion = input(mensaje).lower()
    return opcion



def ingreso_de_texto(mensaje):
    '''
    Esta función se utiliza en todas las funciones donde se le pide al usuario que ingrese el nombre de una película (ya sea para la alta, baja o modificación).
    La función incluye el ingreso por teclado del nombre y la verficación de que el mensaje no se ingrese vacío.
    Hecha por: Oriana Nayla Herrera
    '''
    nombre_pelicula = input(mensaje)
    while nombre_pelicula == "":
        print("No ingresó nada. Por favor, ",end="")
        nombre_pelicula = input(mensaje)
    return nombre_pelicula



def dos_opciones(mensaje):
    '''
    Esta función se utiliza cuando el usuario debe de elegir entre 2 opciones.
    Incluye el ingreso de los números correspondientes a las opciones y su posterior validación: se verifica que sea un número (si lo es se lo convierte en un int) y si no lo es o es diferente de lo que se solicita, se pide que lo intente nuevamente.
    Hecha por: Oriana Nayla Herrera
    '''
    confirmar = input(mensaje)

    while confirmar != 1 and confirmar != 2:
        if confirmar.isdigit():
            confirmar = int(confirmar)
        if confirmar != 1 and confirmar != 2:
            print("Ingrese una opción válida.\n")
            confirmar = input(mensaje)
    return confirmar



def validacion_sala_duracion(mensaje):
    '''
    Se utiliza en los datos que tienen la misma validación.
    Esta función pide un dato y lo valida: verifica que no sea texto o que no sea menor o igual a 0.
    Hecha por: Oriana Nayla Herrera
    '''
    valor = input(mensaje)
    while valor.isalpha() or (int(valor) <= 0):
        print("El valor ingresado es inválido, intente de nuevo. ",end="")
        valor = input(mensaje)
    valor = int(valor)
    return valor



def validacion_sala_duracion_menosuno(mensaje):
    '''
    Se utiliza en los datos que tienen la misma validación
    Esta función pide un dato y lo valida: verifica que no sea texto, que no sea menor o igual a 0, o si es diferente de -1.
    Hecha por: Oriana Nayla Herrera
    '''
    valor = input(mensaje)
    while valor.isalpha() or (int(valor) <= 0 and int(valor) != -1):
        print("El valor ingresado es inválido, intente de nuevo. ",end="")
        valor = input(mensaje)
    valor = int(valor)
    return valor



def titulos(matriz):
    '''
    La función imprime la información de las peliculas guardadas en la matriz.
    Hecha por: Oriana Nayla Herrera
    '''
    print("\nTítulos:\n")
    for i in range(0,len(matriz)):
        print(f"\nNombre:{matriz[i][0].title()}.  Género: {matriz[i][1]}. Duración: {matriz[i][2]}. Sala: {matriz[i][3]}. Cantidad de entradas: {matriz[i][4]}. Precio promedio: {matriz[i][5]}. Estado: {matriz[i][6]}.")
        

def imprimir_estados():
    '''
    Esta función imprime el mesaje que informa los estados posibles de la película.
    Hecha por: Oriana Nayla Herrera
    '''
    print("Estados posibles: [1] En cartelera. [2] Próximo estreno. [3] Función especial. [4] Finalizada.")

def imprimir_generos():
    '''
    Esta función imprime el mesaje que informa los géneros disponibles de la película.
    Hecha por: Oriana Nayla Herrera
    '''
    print("\nGeneros disponibles: [1] Acción. [2] Aventura. [3] Comedia. [4] Drama. [5] Ciencia Ficción. [6] Terror. [7] Animación. [8] Documental.")
        
def guiones(mensaje):
    '''
    La función se encarga de imprimir los mensajes (preferiblemente títulos), con guiones arriba y abajo como un marco o división. Se toma el mensaje y se imprime con estas características.
    Hecha por: Oriana Nayla Herrera
    '''
    print("\n---------------------------------------\n",mensaje,"\n---------------------------------------\n")

def alta_manual(matriz,lista_genero,lista_estados):
    '''
    Esta función consiste en pedirle al usuario que ingrese los datos de las películas y que a medida que se van ingresando, se vayan agregando a una lista que corresponde a la pelicula, que a su vez se va agregar a la matriz.
    Se le va a consultar al usuario si va a continuar ingresando más películas.
    Hecha por: Oriana Nayla Herrera
    '''
    respuesta = "si" #empezamos con un si ya definido para que entre directo al ciclo while
        
    while respuesta == "si":
            
        guiones("ALTA DE PELÍCULAS")

        lista_datos_de_la_pelicula = []
            
        #Nombre de la pelicula
        nombre_pelicula = ingreso_de_texto("Ingrese el nombre de la película: ")
        nombre_pelicula = darle_formato_a_los_Strings(nombre_pelicula)
        lista_datos_de_la_pelicula.append(nombre_pelicula)

        #Generos
        imprimir_generos()
        genero = input("Ingrese el género de la película (número): ")
        while genero.isalpha() or (int(genero) >= 9 or int(genero) < 1):
            print("\n¡Valor fuera de rango, género incorrecto!")
            imprimir_generos()
            genero = input("Ingrese el género de la película (número): ")
        genero = int(genero)

        nombre_del_genero = lista_genero[genero-1] #la ubicación del género dentro de la lista siempre va a ser una unidad mas chica
        lista_datos_de_la_pelicula.append(nombre_del_genero)

        #Duración
        duracion_pelicula = validacion_sala_duracion("\nIngrese la duración de la pelicula (en minutos): ") 
        lista_datos_de_la_pelicula.append(duracion_pelicula)

        #Sala
        sala = validacion_sala_duracion("\nIngrese el número de la sala: ")
        lista_datos_de_la_pelicula.append(sala)

        #Entradas
        cantidad_entradas = input("\nIngrese la cantidad de entradas vendidas: ")
        while cantidad_entradas.isalpha() or (int(cantidad_entradas) < 0):
            cantidad_entradas = input("La cantidad de entradas es inválida, intente de nuevo.\nCantidad de entradas: ")
        cantidad_entradas = int(cantidad_entradas)

        lista_datos_de_la_pelicula.append(cantidad_entradas)

        #Precio
        precio_promedio = input("\nIngrese el precio de la entrada: ")
        while precio_promedio.isalpha() or (float(precio_promedio) < 0):
            precio_promedio = input("El valor de las entradas es inválido, intente de nuevo.\n Precio de la entrada: ")
        precio_promedio = float(precio_promedio)

        lista_datos_de_la_pelicula.append(precio_promedio)

        #Estados
        imprimir_estados()
        opcion = input("Ingrese el estado de la cartelera: ")
        while opcion.isalpha() or (int(opcion) > 4 or int(opcion) < 1):
            print("\nDicha opción no existe, intente de nuevo. ")
            imprimir_estados()
            opcion = input("Ingrese el estado de la cartelera: ")
        opcion = int(opcion)

        texto_estado = lista_estados[opcion-1] #la ubicación del estado dentro de la lista siempre va a ser una unidad mas chica
        lista_datos_de_la_pelicula.append(texto_estado)
            
        #Agregar a la matriz
        matriz.append(lista_datos_de_la_pelicula)

        #Definir continuidad del ciclo while
        respuesta = continuidad("\n¿Va a seguir ingresando películas? (respuesta: 'si' o 'no'): ")



def alta_aleatoria(matriz,lista_genero,lista_estados,lista_letras_aleatorias):
    '''
    Esta función se encarga de generar valores aleatorios para un versión de pruebas. A lo largo de la misma se van generando los valores aleatorios, se le va informando al usuario las limitaciones y los valores generados y se van agregando a la lista de la pelicula que luego se va a agregar a la matriz.
    Se le va a consultar al usuario si va a seguir generando películas.
    Hecha por: Oriana Nayla Herrera
    '''
    respuesta = "si" #empezamos con un si ya definido para que entre directo al ciclo while
        
    while respuesta == "si":
        guiones("ALTA DE PELÍCULAS")
        print("-Versión Pruebas\n")

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

        respuesta = continuidad("\n¿Va a seguir generando valores aleatorios? (respuesta: 'si' o 'no'): ")



def alta_peliculas(matriz):
    '''
    Esta función busca que se ingresen películas y que, a medida que eso ocurra, se vayan agregando a la matriz.
    Se pueden ingresar manualmente o aleatoriamente de acuerdo a lo que prefiera el usuario.
    Ejemplo de como quedaría:

    matriz = [

        ["Avatar","Ciencia Ficcion",160,14,25,1000.0,"En cartelera"],
        ["x","Accion",120,12,35,2000.0,"Finalizada"]
    ]
    Hecha por: Oriana Nayla Herrera
    '''
    #Definimos listas
    lista_genero = ["Acción","Aventura","Comedia","Drama","Ciencia Ficción","Terror","Animación", "Documental"]
    lista_estados = ["En cartelera","Próximo estreno","Función especial","Finalizada"]
    lista_letras_aleatorias = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    


    guiones("ALTA DE PELICULAS")
    datos = dos_opciones("Los datos:\n[1] Van a ingresarse por teclado.\n[2] Van a generarse automáticamente (versión para pruebas).\nSu respuesta: ")
    
    if datos == 1:
        alta_manual(matriz,lista_genero,lista_estados)
    elif datos == 2:
        alta_aleatoria(matriz,lista_genero,lista_estados,lista_letras_aleatorias)       



def baja_peliculas(matriz):
    '''
    [baja_peliculas]
    Esta función permite eliminar una película del catálogo. Primero muestra todas las películas registradas, luego pide el nombre de la película que se quiere borrar, la busca en la lista y, si existe y está marcada como "Finalizada", pide una confirmación antes de eliminarla. Esto evita que se borren películas por error o que se eliminen películas que todavía siguen en cartelera.
    Hecha por: Valeria Paoletti
    '''
    guiones("BAJA PELÍCULAS")

    if len(matriz) == 0:
        print("\n¡La matriz está vacía!")
    else:
        opcion = "si" #inicializamos en si para que entre directo al ciclo while
        while opcion == "si":

            titulos(matriz)

            nombre_de_la_pelicula_input = ingreso_de_texto("Ingrese el nombre de la película: ")
            nombre_de_la_pelicula = darle_formato_a_los_Strings(nombre_de_la_pelicula_input)

            posicion_de_pelicula_a_eliminar = busqueda_de_la_pelicula(matriz,nombre_de_la_pelicula)


            if posicion_de_pelicula_a_eliminar != -1:
                
            

                if matriz[posicion_de_pelicula_a_eliminar][6] == "Finalizada":
                    

            

                    print("¿SEGURO QUE QUIERE ELIMINAR ESTA PELICULA?")

                    confirmar = dos_opciones("Ingrese [1] si quiere eliminar la película o [2] cancelar operación: ")

                    if confirmar == 1:
                        
                        matriz.pop(posicion_de_pelicula_a_eliminar)
                        print("¡La película se eliminó exitosamente!")

                    
                    else:

                        print("¡La operación se canceló!")

                
                else:

                    print("¡La pelicula no esta finalizada!")
        
            else:

                print("La película ingresada no está en el catálogo.")

            opcion = continuidad("¿Va a seguir eliminando películas? (respuesta: 'si' o 'no'): ")



def busqueda_de_la_pelicula(matriz,nombre_de_la_pelicula):
    '''
    [Esta función se encarga de buscar una película dentro de la lista. Recorre todas las películas registradas y compara sus nombres con el que ingresó el usuario. Si la encuentra, devuelve la posición donde está guardada; si no la encuentra, devuelve -1 para indicar que la película no existe en el catálogo.n]
    Hecha por: Emma Mealla
    '''
    pos = -1
    contador = 0

    while pos == -1 and contador < len(matriz):

        if matriz[contador][0] == nombre_de_la_pelicula:
            pos = contador
        
        contador = contador + 1
  
    return pos



def modificar_peliculas(matriz):
    '''
    [Esta función permite actualizar los datos de una película ya registrada. Primero busca la película que el usuario quiere modificar y, si la encuentra, ofrece la posibilidad de cambiar cada uno de sus datos (nombre, género, duración, sala, entradas, precio y estado). También permite dejar un dato sin cambios si así se desea.]
    Hecha por: Emma Mealla
    '''
    guiones("MODIFICAR PELÍCULAS")

    if len(matriz) == 0:
        print("\n¡La matriz está vacía!")
    else:
        opcion = "si" #inicializamos en si para que ingrese directamente al ciclo while
        while opcion == "si":

            #imprimir los titulos
            titulos(matriz)


            titulo_de_la_pelicula_a_modificar = ingreso_de_texto("Ingrese el nombre de la película a modificar: ")
            titulo_de_la_pelicula_a_modificar = darle_formato_a_los_Strings(titulo_de_la_pelicula_a_modificar)

            posicion_de_la_pelicula = busqueda_de_la_pelicula(matriz,titulo_de_la_pelicula_a_modificar)

            if posicion_de_la_pelicula != -1:
                
                lista_genero = ["Acción","Aventura","Comedia","Drama","Ciencia Ficción","Terror","Animación", "Documental"]
                lista_estados = ["En cartelera","Próximo estreno","Función especial","Finalizada"]
            
                nombre_de_la_pelicula = ingreso_de_texto("Ingrese el nuevo nombre de la pelicula o ingrese un -1 para para no cambiar este atributo: ")
                nombre_de_la_pelicula = darle_formato_a_los_Strings(nombre_de_la_pelicula)

                if nombre_de_la_pelicula != "-1":
                    matriz[posicion_de_la_pelicula][0] = nombre_de_la_pelicula

                imprimir_generos()
                genero = input("Ingrese el genero de la pelicula o ingrese un -1 para para no cambiar este atributo: ")

                
                while genero.isalpha() or (int(genero) >= 9 or int(genero) < 1) and (int(genero) != -1):
                    print("El género ingresado es incorrecto!")
                    imprimir_generos()
                    genero = input("Ingrese el género de la película: ")
                genero = int(genero)

                if genero != -1:
                    texto_del_genero = lista_genero[genero-1]
                    matriz[posicion_de_la_pelicula][1] = texto_del_genero



                duracion_pelicula = validacion_sala_duracion_menosuno("Ingrese la duración de la película o ingrese un -1 para para no cambiar este atributo: ")

                if duracion_pelicula != -1:
                    matriz[posicion_de_la_pelicula][2] = duracion_pelicula

                sala = validacion_sala_duracion_menosuno("Ingrese el número de la sala o ingrese un -1 para para no cambiar este atributo: ")
                
                if sala != -1:
                    matriz[posicion_de_la_pelicula][3] = sala
                
                cantidad_entradas = input("Ingrese la cantidad de entradas vendidas o ingrese un -1 para para no cambiar este atributo: ")
                while cantidad_entradas.isalpha() or (int(cantidad_entradas) < 0) and (int(cantidad_entradas) != -1):
                    cantidad_entradas = input("¡El valor ingresado es inválido! Por favor, ngrese la cantidad de entradas vendidas o ingrese un -1 para para no cambiar este atributo: ")
                cantidad_entradas = int(cantidad_entradas)

                if cantidad_entradas != -1:
                    matriz[posicion_de_la_pelicula][4] = cantidad_entradas

                precio_promedio = input("Ingrese el precio de la entrada o ingrese un -1.0 para para no cambiar este atributo: ")
                while precio_promedio.isalpha() or (float(precio_promedio) <= 0) and (int(precio_promedio) != -1):
                    precio_promedio = input("¡El valor ingresado es inválido! Por favor, ingrese el precio de la entrada o ingrese un -1.0 para para no cambiar este atributo: ")
                precio_promedio = float(precio_promedio)

                if precio_promedio != -1.0:

                    matriz[posicion_de_la_pelicula][5] = precio_promedio


                imprimir_estados()
                opcion = input("Ingrese el estado de la cartelera o ingrese un -1 para para no cambiar este atributo: ")

                while opcion.isalpha() or ((int(opcion) > 4) or (int(opcion) < 1)) and (int(opcion) != -1):
                    print("¡Opción incorrecta!")
                    imprimir_estados()
                    opcion = input("Ingrese el estado de la cartelera: ")
                opcion = int(opcion)

                if opcion != -1:
                    texto_estado = lista_estados[opcion-1]
                    matriz[posicion_de_la_pelicula][6] = texto_estado
                    
                print("¡¡¡Se modificó la película con éxito!!!")


            else:
                print("La película ingresada no existe, ¡pruebe con otra!")
            
            opcion = continuidad("¿Va a seguir modificando películas? (respuesta: 'si' o 'no'): ")



def informe(matriz):
    '''
    [Esta función genera un informe con todas las películas registradas. Antes de mostrarlas, las ordena según la cantidad de entradas vendidas, de mayor a menor. Si dos películas tienen la misma cantidad de ventas, las organiza alfabéticamente por nombre. Luego muestra toda la información de cada película de forma ordenada.]
    Hecha por: Axel Rodriguez
    '''
    guiones("INFORME")

    if len(matriz) == 0:
        print("\n¡La matriz está vacía!")
    else:
        ordenar_las_peliculas(matriz)
        titulos(matriz)
