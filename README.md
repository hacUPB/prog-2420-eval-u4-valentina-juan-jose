[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WQjBwS08)
# Unidad 4
---
## Documentación del proyecto
Nombre: Valentina Giraldo-Juan José Sánchez  
ID: 000464879-00049215

### Documentación del proyecto

Se explicará las funciones y el paso a paso del código realizado.

1. Lo principal que se debe hacer es importar las librerías que se usaran para el código, en este caso se uso para graficar, para sacar estadisticas y para que identifique los archivos csv. 

![Imagen 1](<Imagen de WhatsApp 2024-11-08 a las 23.00.43_32dc031f.jpg>)

2. Se empezó a escribir funciones 
- función listar_archivos ()
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.01.10_7a577406.jpg>)
Esta se utilizó para que muestre un mensaje informativo sobre los archivos que el programa puede encontrar 

-Función contar_palabras_txt(nombre_archivo)
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.01.49_3d7dcc9a.jpg>)
con esta funcion se busca abrir el archivo en modo lectura, leer todo el contenido del archivo, separar el contenido del archivo en palabras usando split() que divide el texto por espacios, e imprimir el numero total de palabras utilizando len(palabras)

-Función reemplazar_palabra_txt(nombre_archivo, palabra_antigua, palabra_nueva)
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.02.13_10f30878.jpg>)
esta funcion abre el archivo en modo lectura, lee el contenido y lo guarda, reempalaza las palabras antiguas por las palabras nuevas usando replace() y luego reabre el archivo en modo escritura, guarda el contenido nuevo con los reemplazos y lo cierra

-Función contar_caracteres_txt(nombre_archivo)
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.02.58_2deb0c41.jpg>)
esta funcion abre el archivo en modo lectura, lee el contenido y lo guarda, calcula el numero total de caracteres con len(contenido), luego calcula el numero de caracteres sin los espacios utilizando replace para eliminar los espacios y luego contar la longitud del nuevo texto, finalmente imprime ambos valores. 

-Función mostrar_primeras_filas_csv(nombre_archivo)
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.06.29_4f0e32a8.jpg>)
con esta funcion se pretende abrir el archivo csv en modo lectura, convertir las filas leidas en una lista, imprimir las primeras 15 filas del archivo csv.

-Función calcular_estadisticas_csv(nombre_archivo, columna)
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.06.51_05172eaa.jpg>)
se busca abrir el archivo csv en modo lectura, leer la primera fila para obtener los nombres de las columnas, luego se extraen los datos de la columna especificada (usando el índice columna), asegurándose de que los datos sean números mediante el método isdigit(). También calcula y muestra las estadísticas básicas de la columna usando:Promedio: sum(columna_datos) / len(columna_datos),Mediana: Usando la función statistics.median().,Máximo: max(columna_datos)Mínimo: min(columna_datos)

-Función graficar_columna_csv(nombre_archivo, columna)
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.07.11_4ad4dac8.jpg>)
con esta funcion se leen los datos de la columna seleccionada del archivo CSV, se filtran los valores numéricos de la columna y los guarda en una lista (columna_datos).Además, utiliza la librería matplotlib.pyplot para crear un gráfico de línea de los datos en esa columna, agrega un título y etiquetas a los ejes del gráfico y finalmente muestra el gráfico generado.

-La función principal main() es para que llame a todas las funciones y las ejecute.Con esta se proporciona un  menú interactivo que permita al usuario elegir qué tipo de operación desea realizar. 
![alt text](<Imagen de WhatsApp 2024-11-08 a las 23.07.49_2c065894.jpg>)

