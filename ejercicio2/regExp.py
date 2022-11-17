#!/usr/bin/env python3
import os
import re
import sys
import subprocess

parametroIngresado=sys.argv[1::]
parametroValido=['-e', '-a']

#Full Path donde se ubica el archivo auxiliar
fullpath='/home/administrator/obligatorio/ejercicio2_python/aux'

# En Aux, se debe escribir la ruta Absoluta a /tmp/
with open(fullpath,'w') as salida:
    res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o", stdout=salida, shell=True,text=True,)


    formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
    os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo



#Probar como Reordenar la salida de TMP por salida STDOUT
# Lo identifico
filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

#Imprimir Linea completa donde esta esa ocurrencia.
filename = open(formatoppid, 'r')
expresionRegular=0
for a in parametroIngresado:
    expresionRegular+=1
    if a == parametroValido[0]:
        print(parametroIngresado[expresionRegular])
        for line in filename:
            if re.search(parametroIngresado[expresionRegular], line):
                print(line)

