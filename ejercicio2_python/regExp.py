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

#############################################
#                   e
#############################################

parametroIngresado=sys.argv[1::]

encontro=0
num=0
for i in parametroIngresado:
    expresionRegular=i
    num+=1
    anterior=num-1
    parametroAnteriorIngresado=sys.argv[anterior]

    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
        filename = open(filename, 'r')
        for line in filename:
            if re.search(expresionRegular, line):
                encontro+=1
                coincidencia=line
                print(coincidencia)
            else:
                encontro+=0

if encontro <= 0:
    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
    sys.exit(25)
