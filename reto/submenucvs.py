import csv
import matplotlib.pyplot as plt

def submenu_csv():
    filename = "archivo_satena_reto.csv"

    while True:
        print("1. Mostrar las 15 primeras filas")
        print("2. Graficar una columnas")
        print("3. Volver al menú principal")
        opcion_csv = input("Seleccione una opción: ")

        match opcion_csv:
            case '1':
                mostrar_primeras_filas(filename)
            case '2':
                graficar_columna(filename)
            case '3':
                break
            case _:
                print("Opción no válida.")

def mostrar_primeras_filas(filename):
    
    with open(filename, 'r', encoding='utf-8') as f:
        lectura_filas = csv.reader(f)
        print("Primeras 15 Filas")
        for i, row in enumerate(lectura_filas):
            if i >= 15:
                break
            print(f"Fila {i}: {row}")
   
def _cargar_columna(filename):
    """Función auxiliar interna para no repetir código"""
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Leer el encabezado
        columnas = next(reader)
        print("Columnas disponibles:")
        for i, nombre_columna in enumerate(columnas):
            print(f"  [{i}] {nombre_columna}")

        indice_columna = int(input("Seleccione el ÍNDICE de la columna: "))

        datos_columna = []
        for fila in reader:
            
            # Intentamos tomar el dato y convertirlo a float
            valor = float(fila[indice_columna])
            datos_columna.append(valor)

        return datos_columna, columnas[indice_columna]


def graficar_columna(filename):
    datos_columna, nombre_columna = _cargar_columna(filename)

    ##esta parte me ayude con la ia para poder hacer los graficos de el archivo csv

    # --- 1. Gráfico de Dispersión ---
    # Usamos el índice de la fila como eje X
    eje_x_dispersion = range(len(datos_columna)) 
    
    plt.figure(figsize=(10, 6))
    plt.scatter(eje_x_dispersion, datos_columna, color='teal', alpha=0.5)
    plt.title(f'Gráfico de Dispersión: {nombre_columna}')
    plt.xlabel('Índice del Dato')
    plt.ylabel(nombre_columna)
    plt.grid(True)
    plt.show()
    
    ##esta parte me ayude con la ia para poder hacer los graficos de el archivo csv
    
    # --- 2. Gráfico de Barras (Histograma) ---
    # Reorganizar los datos (un histograma es la mejor forma de "reorganizar")
    plt.figure(figsize=(10, 6))
    # 'bins=30' divide el rango de datos en 30 "barras"
    plt.hist(datos_columna, bins=30, color='darkorange', edgecolor='black')
    plt.title(f'Histograma (Distribución) de: {nombre_columna}')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True, axis='y')
    plt.show()