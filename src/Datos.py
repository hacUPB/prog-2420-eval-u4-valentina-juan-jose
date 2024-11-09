import csv
import statistics
import matplotlib.pyplot as plt

# Función para mostrar los archivos disponibles
def listar_archivos():
    print("El archivo CSV esperado debe llamarse 'AMVA_Accidentalidad_20191022_2.csv'.")
    print("Asegúrate de que esté en la misma carpeta que este programa.")

# Función para contar palabras en un archivo de texto
def contar_palabras_txt(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    
    palabras = contenido.split()
    print("Número de palabras:", len(palabras))

# Función para reemplazar una palabra por otra en un archivo de texto
def reemplazar_palabra_txt(nombre_archivo, palabra_antigua, palabra_nueva):
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    
    contenido = contenido.replace(palabra_antigua, palabra_nueva)
    
    archivo = open(nombre_archivo, 'w')
    archivo.write(contenido)
    archivo.close()
    
    print(f"Se reemplazó '{palabra_antigua}' por '{palabra_nueva}' en el archivo.")

# Función para contar caracteres en un archivo de texto
def contar_caracteres_txt(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()
    
    total_caracteres = len(contenido)
    caracteres_sin_espacios = len(contenido.replace(" ", ""))
    
    print("Número total de caracteres:", total_caracteres)
    print("Número de caracteres sin espacios:", caracteres_sin_espacios)

# Función para mostrar las primeras 15 filas de un archivo CSV
def mostrar_primeras_filas_csv(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    lector_csv = csv.reader(archivo)
    filas = list(lector_csv)
    archivo.close()
    
    print("Primeras 15 filas del archivo:")
    for i, fila in enumerate(filas[:15]):
        print(f"Fila {i+1}: {fila}")

# Función para calcular estadísticas de una columna en un archivo CSV
def calcular_estadisticas_csv(nombre_archivo, columna):
    archivo = open(nombre_archivo, 'r')
    lector_csv = csv.reader(archivo)
    encabezado = next(lector_csv)
    
    columna_datos = []
    for fila in lector_csv:
        if fila[columna].isdigit():
            columna_datos.append(float(fila[columna]))
    
    archivo.close()
    
    print("Estadísticas de la columna:", encabezado[columna])
    print("Número de datos:", len(columna_datos))
    print("Promedio:", sum(columna_datos) / len(columna_datos))
    print("Mediana:", statistics.median(columna_datos))
    print("Máximo:", max(columna_datos))
    print("Mínimo:", min(columna_datos))

# Función para graficar una columna en un archivo CSV
def graficar_columna_csv(nombre_archivo, columna):
    archivo = open(nombre_archivo, 'r')
    lector_csv = csv.reader(archivo)
    encabezado = next(lector_csv)
    
    columna_datos = []
    for fila in lector_csv:
        if fila[columna].isdigit():
            columna_datos.append(float(fila[columna]))
    
    archivo.close()
    
    plt.plot(columna_datos)
    plt.title(f"Gráfica de la columna: {encabezado[columna]}")
    plt.xlabel("Índice")
    plt.ylabel("Valores")
    plt.show()

# Función principal
def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar archivos")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            listar_archivos()
        
        elif opcion == '2':
            nombre_archivo_txt = input("Nombre del archivo de texto: ")
            print("\n--- Submenú para archivos de texto (.txt) ---")
            print("1. Contar número de palabras")
            print("2. Reemplazar una palabra por otra")
            print("3. Contar número de caracteres")
            
            opcion_txt = input("Elige una opción: ")
            
            if opcion_txt == '1':
                contar_palabras_txt(nombre_archivo_txt)
            elif opcion_txt == '2':
                palabra_antigua = input("Palabra a reemplazar: ")
                palabra_nueva = input("Nueva palabra: ")
                reemplazar_palabra_txt(nombre_archivo_txt, palabra_antigua, palabra_nueva)
            elif opcion_txt == '3':
                contar_caracteres_txt(nombre_archivo_txt)
        
        elif opcion == '3':
            nombre_archivo_csv = 'AMVA_Accidentalidad_20191022_2.csv'
            print("\n--- Submenú para archivos CSV ---")
            print("1. Mostrar las primeras 15 filas")
            print("2. Calcular estadísticas de una columna")
            print("3. Graficar una columna")
            
            opcion_csv = input("Elige una opción: ")
            
            if opcion_csv == '1':
                mostrar_primeras_filas_csv(nombre_archivo_csv)
            elif opcion_csv == '2':
                columna = int(input("Número de la columna a analizar (empezando desde 0): "))
                calcular_estadisticas_csv(nombre_archivo_csv, columna)
            elif opcion_csv == '3':
                columna = int(input("Número de la columna a graficar (empezando desde 0): "))
                graficar_columna_csv(nombre_archivo_csv)
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break

# Ejecutar el programa
main()