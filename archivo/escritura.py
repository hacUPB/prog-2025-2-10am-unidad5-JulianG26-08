'''
#con modo w
ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos"
#\ se utiliza para comandos de texto

nombre_archivo = "frutas.txt"
modo = "w" # solo escritura _ sobreescribe
fp = open (ubicacion + "\\" + nombre_archivo , modo ,encoding= "utf-8")

frase = input("por favor ingresa una frase : ")
fp.write (frase + "\n")
#solicitar al usuario una variable entera y una float al usuario y la escriben en el archivo 

peso = int(input("escribe tu peso : "))
altura = float(input("ingresa tu altura: "))

fp.write(frase +"\n")
fp.write(str(peso) + "\n")
fp.write(str(altura) + "\n")




fp.close()
'''

'''
#con modo a
ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos"
#\ se utiliza para comandos de texto

nombre_archivo = "frutas2.txt"
modo = "a" 
fp = open (ubicacion + "\\" + nombre_archivo , modo ,encoding= "utf-8")

frase = input("por favor ingresa una frase : ")
fp.write (frase + "\n")
#solicitar al usuario una variable entera y una float al usuario y la escriben en el archivo 

peso = int(input("escribe tu peso : "))
altura = float(input("ingresa tu altura: "))

fp.write(frase +"\n")
fp.write(str(peso) + "\n")
fp.write(str(altura) + "\n")




fp.close()
'''

#con modo w
ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivos"
#\ se utiliza para comandos de texto

nombre_archivo = "frutas3.txt"
modo = "x" 
fp = open (ubicacion + "\\" + nombre_archivo , modo ,encoding= "utf-8")

frase = input("por favor ingresa una frase : ")
fp.write (frase + "\n")
#solicitar al usuario una variable entera y una float al usuario y la escriben en el archivo 

peso = int(input("escribe tu peso : "))
altura = float(input("ingresa tu altura: "))

fp.write(frase +"\n")
fp.write(str(peso) + "\n")
fp.write(str(altura) + "\n")




fp.close()