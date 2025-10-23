import csv
lista1 = [25,33,55,66,77,88]
lista2 = ['julian', 'pablo', 'juan', 'negro']
with open('pepe.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['pablo', 25, 'medellin'])
    escritor.writerow(['jesus', 100, 'jerusalen'])
    escritor.writerow(['1','2','3'])
    escritor.writerow(lista1)
    escritor.writerow(lista2)


