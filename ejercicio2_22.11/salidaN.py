#!/usr/bin/env python3
import os
import re
import sys
import subprocess


#Full Path donde se ubica el archivo auxiliar
fullpath='/home/administrator/obligatorio/ejercicio2_python/aux'

# En Aux, se debe escribir la ruta Absoluta a /tmp/
with open(fullpath,'w') as salida:
    res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o", stdout=salida, shell=True,text=True,)


    formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
    os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo


# Lo identifico
filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

######################################
#               N
######################################

#Imprimir Linea completa donde esta esa ocurrencia.
filename = open(filename, 'r')
for line in filename:
    if not re.findall(r"^Cantidad de archivos listados:", line):
        print(line)

