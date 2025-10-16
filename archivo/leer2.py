variable = open("./archivo/julian.txt","r",encoding="UTF-8")

# variable.readline()
# variable.readline()
# variable.read(11)
variable.seek(10)
datos = variable.readline()

variable.close()
print (variable)