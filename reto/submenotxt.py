import os
import csv
import matplotlib.pyplot as plt


def submenu_txt():
    filename = "julian.txt"
    with open(filename, 'r', encoding='utf-8') as fp:
        contenido = fp.read()
    print(f"Archivo '{filename}' cargado exitosamente.")

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
                reemplazar_palabra(filename)
                with open(filename, 'r', encoding='utf-8') as fp:
                    contenido = fp.read()
            case '3':
                histograma_vocales(contenido)
            case '4':
                break
            case _:
                print("Opción no válida.")

    def contar_palabras_caracteres(texto):
        palabras = texto.split()
        num_palabras = len(palabras)
        print(f"Número de palabras: {num_palabras}")
        num_caracteres_con_espacios = len(texto)
        print(f"Caracteres : {num_caracteres_con_espacios}")
        

    def reemplazar_palabra(filename):
        palabra_buscar = input("Palabra a buscar: ")
        palabra_reemplazar = input("Reemplazar por: ")
        with open(filename, 'r', encoding='utf-8') as fp:
            contenido = fp.read()
        nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazar)
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(nuevo_contenido)
        print(f"Se reemplazó '{palabra_buscar}' por '{palabra_reemplazar}' exitosamente.")

    def histograma_vocales(texto):
        vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for char in texto.lower():
            if char in vocales:
                vocales[char] += 1
        nombres_vocales = list(vocales.keys())
        conteo_vocales = list(vocales.values())

        print(f"Conteo de vocales: {vocales}")

        plt.figure(figsize=(8, 5))
        bars = plt.bar(nombres_vocales, conteo_vocales, color='skyblue')
        plt.title('Histograma de Ocurrencia de Vocales')
        plt.xlabel('Vocal')
        plt.ylabel('Frecuencia')
        for bar in bars:
            yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom')
        plt.show()