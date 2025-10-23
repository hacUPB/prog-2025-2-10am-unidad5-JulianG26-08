'''
import csv

with open('C:\\Users\\B09S202est\\Documents\\Programacion-2025\\prog-2025-2-10am-unidad5-JulianG26-08\\Libro1.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader

    encabezado = next(lector)
    print(encabezado[0] )
    presion = []
    for fila in lector:          #con el for se itera sobre el objeto para leer
        dato = int(fila[0])
        presion.append(dato)

print (presion)
'''
'''
import csv

with open('C:\\Users\\B09S202est\\Documents\\Programacion-2025\\prog-2025-2-10am-unidad5-JulianG26-08\\Libro1.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader

    encabezado = next(lector)
    print(encabezado[3] )
    densidad = []
    for fila in lector:          #con el for se itera sobre el objeto para leer
        fila [3] = fila[3].replace(',','.')
        dato = float(fila[3])
        densidad.append(dato)

print (densidad)
'''

