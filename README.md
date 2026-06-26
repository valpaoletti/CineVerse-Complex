# CineVerse-Complex
TPO.


## Alcance
Proyecto: CineVerse Complex (Sistema de Gestión Cinematográfica)

<h1>Introducción</h1><br>

CineVerse Complex requiere una solución que permita centralizar la administración y
análisis de información relacionada con películas, funciones y rendimiento comercial
gestionados por el complejo cinematográfico.<br>
Actualmente, gran parte de la información se encuentra distribuida en registros
manuales y planillas independientes, dificultando el control de la programación, la
ocupación de salas y la generación de reportes operativos.<br>
El objetivo del presente proyecto es desarrollar una herramienta interactiva que permita
administrar películas y funciones, mantener información sincronizada y generar
informes de análisis para apoyar la toma de decisiones de supervisores y responsables
de programación.<br>
El desarrollo será realizado de manera incremental mediante dos fases evolutivas,
donde cada versión incorporará nuevas funcionalidades y mejoras sobre la versión
anterior.<br>

<h2>Objetivos del Sistema</h2><br>
El sistema deberá permitir:<br>
• Centralizar la información de películas y funciones.<br>
• Registrar y administrar nuevas películas.<br>
• Modificar información relevante de la programación.<br>
• Eliminar películas que ya no se encuentren en exhibición.<br>
• Generar informes operativos y estratégicos.<br>
• Facilitar el análisis de asistencia y rentabilidad según distintos criterios.<br>
• Mantener una interacción simple, clara y continua para el usuario.<br>

Información Administrada por el Sistema - Para cada película, el complejo registra la siguiente información:<br>

1. Título de la película.<br>
2. Género principal.<br>
3. Duración en minutos.<br>
4. Sala asignada.<br>
5. Cantidad de entradas vendidas.<br>
6. Valor promedio de la entrada.<br>
7. Estado de exhibición.<br>

Descripción de las Piezas de Información del Sistema<br>

<h2>Título de la película - Corresponde al nombre de la película exhibida en el complejo.</h2><br>

Ejemplos:<br>
• Jurassic World<br>
• Avatar<br>
• Intensamente 2<br>
• Superman<br>
No puede quedar vacío.<br>

<h2>Género principal - Indica la categoría principal de la película.</h2><br>

Sólo permitir:<br>

• Acción<br>
• Aventura<br>
• Comedia<br>
• Drama<br>
• Ciencia Ficción<br>
• Terror<br>
• Animación<br>
• Documental<br>

<h2>Duración en minutos - Representa la duración total de la película.</h2><br>
Ejemplos:<br>

• 90 minutos<br>
• 120 minutos<br>
• 165 minutos<br>

Debe ser un número entero positivo.<br>

<h2>Sala asignada - Representa el número de sala donde se proyecta la película.</h2><br>

Ejemplos:<br>
• Sala 1<br>
• Sala 5<br>
• Sala 10<br>

Debe ser un número entero positivo.<br>

<h2>Cantidad de entradas vendidas - Representa la cantidad total de entradas vendidas para la función.<h2/><br>

Ejemplos:<br>
• 25<br>
• 120<br>
• 350<br>
Debe ser un número entero positivo o cero.<br>

<h2>Valor promedio de la entrada - Representa el precio promedio pagado por los espectadores.</h2><br>

Ejemplos:<br>

• 4500.50<br>
• 6200.00<br>
• 7800.75<br>

Debe permitir valores con decimales y no puede ser negativo.<br>

<h2>Estado de exhibición - Indica la situación actual de la película dentro de la cartelera.</h2><br>

Sólo permitir:<br>

• En cartelera<br>
• Próximo estreno<br>
• Función especial<br>
• Finalizada<br>

<h3>Alcance General - El sistema permitirá gestionar películas y funciones mediante operaciones de
administración y generación de reportes.</h3><br>

El producto será entregado en dos versiones evolutivas:<br>

• Fase 1: Gestión inicial y visualización básica.<br>
• Fase 2: Administración completa e informes analíticos.<br>

<h1> FASE 1 – Versión Inicial del Producto</h1>

Objetivo<br>
Construir una primera versión funcional que permita cargar información inicial, navegar
mediante un menú interactivo y visualizar los datos registrados.<br>

Esta primera versión puede tener opciones del menú que aún no están implementadas,
debiendo mostrar un mensaje: "Funcionalidad pendiente".<br>

<h3>Ejemplo de menú</h3>

==================================================<br>
SISTEMA DE GESTIÓN: CINEVERSE COMPLEX<br>
1. Registrar película (Alta)<br>
2. Eliminar película (Baja)<br>
3. Modificar película (Modificación)<br>
4. Informe General – Visualización de los datos<br>
5. Salir<br>
==================================================<br>

Seleccione una opción (1-4 o 5 para salir):<br>

Descripción de las Opciones del Menú<br>

1. Registrar película (Alta)<br>
Permite registrar una o varias películas en el sistema.
Los datos podrán ingresarse por teclado o generarse automáticamente mediante
valores aleatorios para facilitar las pruebas y la carga inicial de información.<br>

2. Eliminar película (Baja)<br>
Permite eliminar una película existente seleccionándola mediante su título.
Antes de realizar la eliminación, el sistema deberá solicitar confirmación al usuario.
Solo podrán eliminarse películas cuyo estado de exhibición sea "Finalizada".<br>

3. Modificar película (Modificación)<br>
Permite modificar uno o más atributos de una película registrada.
La película deberá seleccionarse utilizando su título.<br>

4. Informe General – Visualización de los datos<br>
Muestra un listado de todas las películas registradas en el sistema.
El informe deberá presentar las películas ordenadas de mayor a menor según la
cantidad de entradas vendidas. En caso de igualdad, deberán ordenarse
alfabéticamente por título.<br>

5. Salir<br>
Finaliza la ejecución del sistema.<br>

<h3>Repositorio</h3>
https://github.com/valpaoletti/CineVerse-Complex

