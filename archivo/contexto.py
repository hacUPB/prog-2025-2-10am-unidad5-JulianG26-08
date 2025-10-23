nombre_archivo = "canciones.txt"
ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos"
with open (ubicacion + "\\" +nombre_archivo , "r" , encoding= "utf-8") as archivo:

   lista = archivo.readlines ()        

for c in lista :
   print(c)             

                     