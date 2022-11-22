#!/usr/bin/env python3
import os
import re
import sys
import subprocess



# #Full Path donde se ubica el archivo auxiliar
# fullpath='/home/administrator/obligatorio/ejercicio2_python/aux'

# # En Aux, se debe escribir la ruta Absoluta a /tmp/
# with open(fullpath,'w') as salida:
#     res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o", stdout=salida, shell=True,text=True,)


#     formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
#     os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo



# #Probar como Reordenar la salida de TMP por salida STDOUT
# # Lo identifico
# filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

filename=open('/tmp/filename.txt', 'a')
# filename.close()

borrar = subprocess.run('/home/administrator/obligatorio/ejercicio2_python/borrar.sh')

#os.system(borrar)
#os.remove(filename)
# os.unlink(filename)
# #############################################
# #                   e
# #############################################

# parametroIngresado=sys.argv[1::]

# encontro=0
# num=0
# for i in parametroIngresado:
#     expresionRegular=i
#     num+=1
#     anterior=num-1
#     parametroAnteriorIngresado=sys.argv[anterior]

#     if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
#         filename = open(filename, 'r')
#         for line in filename:
#             if re.search(expresionRegular, line):
#                 encontro+=1
#                 coincidencia=line
#             else:
#                 encontro+=0

# if encontro > 0:
#     print(coincidencia)
# else:
#     print('No se encontro una coincidencia valida')


# borrar='/home/administrator/obligatorio/ejercicio2_python/borrar.txt'
# os.remove(borrar)


