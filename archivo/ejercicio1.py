nombre_archivo = input (" ingrese el nombre del archivo a crear ")

with open (nombre_archivo, "w") as archivo :
    datos = input ( "ingrese los datos que desea escribir en el archivo")
    archivo.write(datos)

with open (nombre_archivo, "r") as archivo :
    contenido = archivo.read ()
    print ("contenido del archivo")
    print (contenido)