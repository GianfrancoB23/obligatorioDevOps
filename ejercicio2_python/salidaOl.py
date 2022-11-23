#!/usr/bin/env python3

import os
import subprocess
import sys

## Ejemplo de prueba con -m -o -r ##

#Nombre y ubicacion
formatoppid = '{}.txt'.format(os.getppid())
#print(formatoppid)

filename='/tmp/'+str(formatoppid)

with open(filename,'w') as salida:
    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o -r "
    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

###########################################################################
#                              Ol
###########################################################################

#Cantidad de lineas totales
num_lines = sum(1 for line in open(filename))

#Crear la lista con nombre de las ubicaciones, de la salida auxiliar.

listaUbicaciones=[]

with open (filename) as fin:
    for line in fin:
        listaUbicaciones.append(line.strip())

#####Con este codigo tengo la Longitud de las lineas del archivo filename PPIDFILE.tmp
caracteresTotales=[]

with open(filename) as infile:
        lines = infile.readlines()
        for line in lines:
            cantCaracter=len(line)
            #print(cantCaracter)
            caracteresTotales.append(cantCaracter)

##Necesito crear una lista con el nombre de los elementos y la cantidad de caracteres.
#Solo debo imprimir 

a = list(set(caracteresTotales))
a.sort(reverse=True)
listaOC = []
for i in a:
    for j in range(0, len(caracteresTotales)):
        if(caracteresTotales[j] == i):
            listaOC.append(listaUbicaciones[j] + '\n')


with open(filename, 'w') as infile:
    #Bucle para ver la salida de lo que busco.
    for x in listaOC:
        infile.write(x)

#######################################
#       Imprime Ol
#######################################

with open(filename) as infile:
    lines = infile.readlines()
    for line in lines:
        print(line)