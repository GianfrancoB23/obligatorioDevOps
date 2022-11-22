#!/usr/bin/env python3

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

##############################################
#                i
##############################################

# Invierto el archivo
invertido=reversed(list(open(filename)))

# Lo voy agregando linea por linea al archivo de forma ordenada
with open(filename, 'w') as infile:
    for line in invertido:
        infile.write(line.rstrip() + '\n')

#######################################
#       Imprime salida i
#######################################

with open(filename) as infile:
    lines = infile.readlines()
    for line in lines:
        print(line)
