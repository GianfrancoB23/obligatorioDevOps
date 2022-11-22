#!/usr/bin/env python3

##############################################################################################################################
#                                                    Modulos                                                                 #
##############################################################################################################################

import sys
import subprocess
import os

##############################################################################################################################
#                                                   Funciones                                                                #
##############################################################################################################################

def ayuda():
    print("Ayuda:")
    print("-m busca de forma recursiva en los fileSystem montados")
    print("-o buscar y contar también archivos ocultos")
    print("-r mostrar y contar solamente archivos regulares")
    print("-n se desplegará, después del listado de archivos encontrados")
    print("-Oa a se ordenarán los caminos absolutos a los archivos en forma alfabética creciente por nombre de archivo")
    print("-Oc listarán los caminos absolutos ordenados por orden alfabético creciente del camino absoluto")
    print("-Ol los caminos absolutos por el largo que tengan en forma creciente")
    print("-i  invertirá el orden del listado de salida, sea cual sea este")
    print("-e Mostrar información de depuración")
    return ayuda

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

def cantidadDeParametrosIncorrectos():
    print("Cantidad de parámetros incorrecta, solo se aceptan los siguientes modificadores:")
    print("-m busca de forma recursiva en los fileSystem montados")
    print("-o buscar y contar también archivos ocultos")
    print("-r mostrar y contar solamente archivos regulares")
    print("-n se desplegará, después del listado de archivos encontrados")
    print("-Oa a se ordenarán los caminos absolutos a los archivos en forma alfabética creciente por nombre de archivo")
    print("-Oc listarán los caminos absolutos ordenados por orden alfabético creciente del camino absoluto")
    print("-Ol los caminos absolutos por el largo que tengan en forma creciente")
    print("-i  invertirá el orden del listado de salida, sea cual sea este")
    print("-e Mostrar información de depuración")
    return cantidadDeParametrosIncorrectos

##############################################################################################################################
#                                                Variables y listas                                                          #
##############################################################################################################################

modificadoresValidos = ['-m', '-o', '-r', '-n', '-Oa', '-Oc', '-Ol', '-i', '-e'] # Verificadores validos en total
modificadoresPython = ['-n', '-Oa', '-Oc', '-Ol', '-i', '-e'] # Verificadores que validos del codigo de Python
sumaModificadorPython=0 # Verificador para validar existencia de modificadores de python
verificacionMOR=("-m", "-o", "-r") # Verificadores de MOR
suma=0 # Verificador para validar existencia de MOR
modificadoresIngresados=sys.argv[1::] # los parametros que se ingresaron, se excluye el primero ya que es el archivo
verificacionUbicacion = 0 # Verifica si se ingreso una ubicacion
error=0 # Valida que los parametros sean los correctos

##############################################################################################################################
#                                                Codigo                                                                      #
##############################################################################################################################

#Full Path donde se ubica el archivo auxiliar
fullpath='/home/administrator/obligatorio/ejercicio2_python/aux'

# En Aux, se debe escribir la ruta Absoluta a /tmp/
with open(fullpath,'w') as salida:
    res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o", stdout=salida, shell=True,text=True,)


    formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
    os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo



#Probar como Reordenar la salida de TMP por salida STDOUT
# Lo identifico
filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

################################################################################
#                                       Oc                                     #
################################################################################

bands= list()

with open (filename) as fin:
    for line in fin:
        bands.append(line.strip())

bands.sort()

with open(filename, 'w') as fout:
    for number, band in enumerate(bands):
        if number not in [0,1,2]:
            fout.write(band + '\n')

#######################################
#       Imprime Oc
#######################################

with open(filename) as infile:
    lines = infile.readlines()
    for line in lines:
        print(line)