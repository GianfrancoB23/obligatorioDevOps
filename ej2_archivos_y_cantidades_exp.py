#!/usr/bin/env python3

##############################################################################################################################
#                                                   Import necesarios                                                        #
##############################################################################################################################

import sys
import subprocess

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

suma=0
modificadoresValidos = ['-m', '-o', '-r', '-n', '-O', '-i', '-e']
verificacionMOR=("-m", "-o", "-r")
modificadoresIngresados=sys.argv[1::]

##############################################################################################################################
#                                                  Codigo principal                                                          #
##############################################################################################################################

print('Argumentos ingresados', modificadoresIngresados)
print()

print("Cantidad de parametros ingresados:", len(modificadoresIngresados))
print()

# Verifico la cantidad de parametros ingresados
if len(modificadoresIngresados) > 10:
    
    cantidadDeParametrosIncorrectos()
    sys.exit(25)

else:

    # Verifico si se solicito ayuda
    for a in modificadoresIngresados:
        if a == "-h":
            #Despliego el menu de ayuda
            ayuda()
            sys.exit()

    # Verifico que sean modificadores validos
    error=0
    for b in modificadoresIngresados:
        for c in modificadoresValidos:
            if b != c:
                error+=1
            else:
                error-=1
        if error == 5:
            error=0
    print("Esto es error al final",error)
    if error > 6:                                   # Cambiar cuando se agreguen los parametros de Oa,Oc,Ol
        parametrosIncorrectos()
        sys.exit(25)

#-m', '-o', '-r', '-n', '-O', '-i', '-e'

# Valido los parametros
for x in modificadoresIngresados:      # Recorre los modificadores
    for i in modificadoresValidos:
        
        # Verifico que los parametros ingresados son los posibles
        if x == i:

            print(modificadoresIngresados)

            for j in modificadoresIngresados:
                if j == verificacionMOR[0]:
                    suma = suma + 1
                elif j == verificacionMOR[1]:
                    suma = suma + 2
                elif j == verificacionMOR[2]:
                    suma = suma + 4

            print("Esto es", suma)

            if suma == 7: 
                print("MOR")
                sys.exit()
            elif suma == 5:
                print("MR")
                sys.exit()
            elif suma == 4:
                print("R")
                sys.exit()
            elif suma == 3:
                print("MO")
                sys.exit()
            elif suma == 2:
                print("O")
                sys.exit()
            elif suma == 1:
                print("M")
                sys.exit()
            elif suma == 0:
                print("Sin parametros ingresados")
                sys.exit()

