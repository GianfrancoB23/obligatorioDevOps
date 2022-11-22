#!/usr/bin/env python3
import os
import re
import sys
import subprocess

modificadoresValidos = ['-m', '-o', '-r', '-n', '-Oa', '-Oc', '-Ol', '-i', '-e'] # Verificadores validos en total
verificacionMOR=("-m", "-o", "-r") # Verificadores de MOR
suma=0 # Verificador para validar existencia de MOR
modificadoresPython = ['-n', '-Oa', '-Oc', '-Ol', '-i', '-e'] # Verificadores que validos del codigo de Python
sumaModificadorPython=0 # Verificador para validar existencia de modificadores de python
modificadoresIngresados=sys.argv[1::] # los parametros que se ingresaron, se excluye el primero ya que es el archivo
verificacionUbicacion = 0 # Verifica si se ingreso una ubicacion
error=0 # Valida que los parametros sean los correctos
fullpath="/home/administrator/obligatorio/ejercicio2_python/aux" #Full Path donde se ubica el archivo auxiliar

def parametrosIncorrectos():
    print("Modificadores inaceptables, solamente se aceptan los siguientes:")
    print("-m busca de forma recursiva en los fileSystem montados")
    print("-o buscar y contar también archivos ocultos")
    print("-r mostrar y contar solamente archivos regulares")
    print("-n se desplegará, después del listado de archivos encontrados")
    print("-Oa a se ordenarán los caminos absolutos a los archivos en forma alfabética creciente por nombre de archivo")
    print("-Oc listarán los caminos absolutos ordenados por orden alfabético creciente del camino absoluto")
    print("-Ol los caminos absolutos por el largo que tengan en forma creciente")
    print("-i  invertirá el orden del listado de salida, sea cual sea este")
    print("-e Mostrar información de depuración")
    return parametrosIncorrectos


presente=0
for i in modificadoresIngresados:
    for x in modificadoresIngresados:
        if i == x:
            presente+=1
            
        else:
            presente+=0

        if presente > 1: 
            parametrosIncorrectos()
            sys.exit()
    presente=0

# if presente == 0:
print("Esta todo ok")



# if presente > 9: 
#     print('Repetido')

# # Verifico que sean modificadores validos
# for b in modificadoresIngresados:
#     for c in modificadoresValidos:
#         vuelta+=1
#         # Como ya se que uno de los modificadores ingresados es una ubicacion, le resto 1 para que no me de error
#         if len(b)>3:
#             error=-1
#         # Si el valor ingresado es diferente de los valores validos sumara un error
#         if b != c:
#             error+=1
#             # print(error)
#             # print('Esta es la vuelta', vuelta)
#         else:   # De lo contrario restara un error
#             error-=1
#             # print(error)
#             # print('Esta es la vuelta', vuelta)
#     vuelta=0
    
#     if error == 7: # Si se encontro que uno de los valores es positivo, reseteara el contador de error para el siguiente parametro
#         error=0

# # Si el valor es mayor a 6, se sabe que no matcheo con ningun verificador valido
# if error > 8:                                   
#     parametrosIncorrectos()
#     sys.exit(25)


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





