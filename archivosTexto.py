from io import open

""" archivo1 = open('archivo.txt', 'a')
archivo1.write('\n saludo IDGS801 nuevo juas juas juas')
archivo1.close()
"""

#Una variable para leer un archivo
archivo1 = open('archivo.txt', 'r')

# #Imprimir en una lista lo que tengo escrito en el archivo
# print(archivo1.read())
# #Leer el archivo desde la posición que queremos
# archivo1.seek(10)

# print(archivo1.read())

#print(archivo1.readlines())

for datos in archivo1.readlines():
    print(datos.rstrip())

archivo1.close()