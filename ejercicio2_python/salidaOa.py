#!/usr/bin/env python3

import sys
import subprocess
import os

## Ejemplo de prueba con -m -o -r ##

#Nombre y ubicacion
formatoppid = '{}.txt'.format(os.getppid())
#print(formatoppid)

filename='/tmp/'+str(formatoppid)

with open(filename,'w') as salida:
    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o -r "
    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

#######################################
#                Oa
#######################################

bands= list()

with open (filename) as fin:
    for line in fin:
        bands.append(line.strip())

bands.sort()

with open(filename, 'w') as infile:
    for number, band in enumerate(bands):
        if number not in [0,1,2]:
            infile.write(band + '\n')

#######################################
#       Imprime Oa
#######################################

with open(filename) as infile:
    lines = infile.readlines()
    for line in lines:
        print(line)