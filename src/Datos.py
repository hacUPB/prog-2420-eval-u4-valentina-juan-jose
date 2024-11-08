
import csv

import matplotlib.pyplot as plt



def contar_palabras(archivo_txt):
    with open(archivo_txt, 'r', encoding='utf-8') as f:
        texto = f.read()
    palabras = texto.split()
    print(f"Número de palabras en el archivo: {len(palabras)}")

def contar_caracteres(archivo_txt):
    with open(archivo_txt, 'r', encoding='utf-8') as f:
        texto = f.read()
    caracteres_con_espacios = len(texto)
    caracteres_sin_espacios = len(texto.replace(' ', ''))
    print(f"Total de caracteres (con espacios): {caracteres_con_espacios}")
    print(f"Total de caracteres (sin espacios): {caracteres_sin_espacios}")

def mostrar_15_filas(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.reader(csvfile)
        for i, fila in enumerate(lector_csv):
            if i >= 15:
                break
            print(fila)



def menu_archivo_txt(archivo_txt):
    while True:
        print("\n--- Menú para archivo de texto ---")
        print("1. Contar número de palabras")
        print("2. Reemplazar una palabra por otra")
        print("3. Contar número de caracteres")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            contar_palabras(archivo_txt)
        elif opcion == '2':
            palabra_a_buscar = input("Ingrese la palabra a buscar: ")
            palabra_nueva = input("Ingrese la palabra nueva: ")
            
        elif opcion == '3':
            contar_caracteres(archivo_txt)
        elif opcion == '4':
            break
        else:
            print("Opción inválida, intente de nuevo.")

def menu_archivo_csv(archivo_csv):
    while True:
        print("\n--- Menú para archivo CSV ---")
        print("1. Mostrar las primeras 15 filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna completa")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_15_filas(archivo_csv)
        
        else:
            print("Opción inválida, intente de nuevo.")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar archivos en la ruta actual")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ruta = input("Ingrese la ruta o deje en blanco para la ruta actual: ")
            
        elif opcion == '2':
            archivo_txt = input("Ingrese el nombre del archivo de texto (.txt): ")
            menu_archivo_txt(archivo_txt)
        elif opcion == '3':
            archivo_csv = input("Ingrese el nombre del archivo CSV (.csv): ")
            menu_archivo_csv(archivo_csv)
        elif opcion == '4':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
