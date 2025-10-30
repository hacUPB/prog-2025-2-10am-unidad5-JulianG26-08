
import os
import csv
from unittest import case
import matplotlib.pyplot as plt
def mostrar_menu_principal():
    print("1. Procesar archivo de texto (.txt)")
    print("2. Procesar archivo CSV (.csv)")
    print("3. Salir")
    
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            return opcion
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def main():
    while True:
        opcion = mostrar_menu_principal()
        
        match opcion:
            case 1:
                
                ubicacion = "C:\\Users\\B09S202est\\Documents\\Programacion-2025\\prog-2025-2-10am-unidad5-JulianG26-08\\reto"
                nombre_archivo = "julian.txt"
                ruta_completa = os.path.join(ubicacion, nombre_archivo)
                
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as fp:
                        contenido = fp.read()
                    print(f"Archivo '{nombre_archivo}' cargado exitosamente.")
                except FileNotFoundError:
                    print(f"Error: No se encontró el archivo {nombre_archivo} en {ubicacion}")
                    continue # Vuelve al menú principal si no encuentra el archivo

                while True:
                    print("1. Contar palabras y caracteres")
                    print("2. Reemplazar una palabra")
                    print("3. Histograma de vocales")
                    print("4. Volver al menú principal")
                    opcion_txt = input("Seleccione una opción: ")

                    match opcion_txt:
                        case '1':
                            contar_palabras_caracteres(contenido)
                        case '2':
                            contenido = reemplazar_palabra(contenido, ubicacion, nombre_archivo)
                        case '3':
                            histograma_vocales(contenido)
                        case '4':
                            break
                        case _:
                            print("Opción no válida.")

            case 2:
                
                ubicacion = "C:\\Users\\B09S202est\\Documents\\Programacion-2025\\prog-2025-2-10am-unidad5-JulianG26-08\\reto"
                nombre_archivo= "archivo_satena_reto.csv"

                while True:
                    print("1. Mostrar las 15 primeras filas")
                    print("2. Graficar una columnas")
                    print("3. Volver al menú principal")
                    opcion_csv = input("Seleccione una opción: ")

                    match opcion_csv:
                        case '1':
                            mostrar_primeras_filas(ubicacion, nombre_archivo)
                        case '2':
                            graficar_columna(ubicacion, nombre_archivo)
                        case '3':
                            break
                        case _:
                            print("Opción no válida.")
                            
            case 3:
                print("Saliendo de la aplicación...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
#txt
def contar_palabras_caracteres(contenido):
    palabras = contenido.split()
    num_palabras = len(palabras)
    print(f"Número de palabras: {num_palabras}")
    num_caracteres_con_espacios = len(contenido)
    print(f"Caracteres : {num_caracteres_con_espacios}")

def reemplazar_palabra(contenido, ubicacion, nombre_archivo):
    palabra_buscar = input("Palabra a buscar: ")
    palabra_reemplazar = input("Reemplazar por: ")
    nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazar)
    
    ruta_completa = os.path.join(ubicacion, nombre_archivo)
    with open(ruta_completa, 'w', encoding='utf-8') as fp:
        fp.write(nuevo_contenido)
        
    print(f"Se reemplazó '{palabra_buscar}' por '{palabra_reemplazar}' ")
    return nuevo_contenido 

def histograma_vocales(contenido):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in contenido.lower():
        if char in vocales:
            vocales[char] += 1
            
    nombres_vocales = list(vocales.keys())
    conteo_vocales = list(vocales.values())

    print(f"Conteo de vocales: {vocales}")

    plt.figure(figsize=(8, 5))
    bars = plt.bar(nombres_vocales, conteo_vocales, color='skyblue')
    plt.title('Histograma de Ocurrencia de Vocales')
    plt.xlabel('Vocal')
    plt.ylabel('Frecuencia')                    #en esta parte de histograma utilize la ia
    
   
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom')
        
    plt.show()

# csv
def mostrar_primeras_filas(ubicacion, nombre_archivo):
    
    ruta_completa = os.path.join(ubicacion, nombre_archivo)
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            lectura_filas = csv.reader(f)
            print("\nPrimeras 15 Filas")
            for i, row in enumerate(lectura_filas):
                if i >= 15:
                    break
                print(f"Fila {i}: {row}")   # en esta parte tenia el error y le pregute a la ia 
    except FileNotFoundError:               # y me dijo que le colocara esto para evitar errores
        print(f"Error: No se encontró el archivo {nombre_archivo} en {ubicacion}")
    except Exception as e:
        print(f"Ocurrió un error al leer el CSV: {e}")

def _cargar_columna(ubicacion, nombre_archivo)
    ruta_completa = os.path.join(ubicacion, nombre_archivo)
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            
            columnas = next(reader)
            print("\nColumnas disponibles:")
            for i, nombre_columna in enumerate(columnas):
                print(f"  [{i}] {nombre_columna}")

            while True:
                try:
                    indice_columna = int(input("Seleccione el ÍNDICE de la columna a graficar: "))
                    if 0 <= indice_columna < len(columnas):
                        break
                    else:
                        print("Índice fuera de rango. Intente de nuevo.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")

            datos_columna = []
            for fila in reader:
                try:
                    valor = float(fila[indice_columna])
                    datos_columna.append(valor)
                except (ValueError, IndexError):
                    continue 

            return datos_columna, columnas[indice_columna]
            #estas partes que son para evitar errores me ayudo la ia
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo} en {ubicacion}")
        return [], ""
    except Exception as e:
        print(f"Ocurrió un error al cargar la columna: {e}")
        return [], ""


def graficar_columna(ubicacion, nombre_archivo):
   
    datos_columna, nombre_columna = _cargar_columna(ubicacion, nombre_archivo)
    
    if not datos_columna:
        print("No hay datos válidos para graficar.")
        return
        
    print(f"Graficando columna: {nombre_columna}")

    # --- 1. Gráfico de Dispersión ---
    eje_x_dispersion = range(len(datos_columna)) 
    
    plt.figure(figsize=(10, 5))
    plt.scatter(eje_x_dispersion, datos_columna, color='teal', alpha=0.5, s=5) 
    plt.title(f'Gráfico de Dispersión: {nombre_columna}')
    plt.xlabel('Índice del Dato')
    plt.ylabel(nombre_columna)
    plt.grid(True)
    plt.show()
    
    # --- 2. Gráfico de Barras (Histograma) ---
    plt.figure(figsize=(10, 5))
    # 'bins=30' divide el rango de datos en 30 "barras"
    plt.hist(datos_columna, bins=30, color='darkorange', edgecolor='black')
    plt.title(f'Histograma (Distribución) de: {nombre_columna}')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True, axis='y')
    plt.show()
