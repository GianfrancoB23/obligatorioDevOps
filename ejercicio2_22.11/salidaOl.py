#!/usr/bin/env python3

import os
import subprocess
import sys

#Full Path donde se ubica el archivo auxiliar
fullpath='/home/administrator/obligatorio/ejercicio2_python/aux'

# En Aux, se debe escribir la ruta Absoluta a /tmp/
with open('aux','w') as salida:
    res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o", stdout=salida, shell=True,text=True,)
    #print(res.stderr) #Respuesta con error.
    formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
    os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

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