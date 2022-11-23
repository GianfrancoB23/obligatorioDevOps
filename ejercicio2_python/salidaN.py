#!/usr/bin/env python3
import os
import re
import sys
import subprocess

## Ejemplo de prueba con -m -o -r ##

#Nombre y ubicacion
formatoppid = '{}.txt'.format(os.getppid())
#print(formatoppid)

filename='/tmp/'+str(formatoppid)

with open(filename,'w') as salida:
    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o -r "
    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

######################################
#               N
######################################

#Imprimir Linea completa donde esta esa ocurrencia.
filename = open(filename, 'r')
for line in filename:
    if not re.findall(r"^Cantidad de archivos listados:", line):
        print(line)

