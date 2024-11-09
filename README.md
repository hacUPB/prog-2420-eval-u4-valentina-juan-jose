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