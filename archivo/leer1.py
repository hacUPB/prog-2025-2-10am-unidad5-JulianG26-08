# abrir el archivo y definir el modo 
archivo = open("./archivo/texto.txt","r")
# leer el archivo
#datos = archivo.read()
# for i in range(5):
#    datos = archivo.readline()
# for datos in archivo:
#     print (datos[0])
datos = archivo.readlines()
print(datos)
#cerrar el archivo
archivo.close()