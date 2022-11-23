#!/usr/bin/env python3

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
