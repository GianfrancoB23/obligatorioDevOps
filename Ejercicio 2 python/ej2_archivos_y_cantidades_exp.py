#!/usr/bin/env python3

##[-n] [-O {a,c,l}] [-i] [-e RegExp] [ Directorio ]

##########################################################################################################################################
#                                                   Funciones                                                                #
##########################################################################################################################################

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
    
##########################################################################################################################################
#                                                            Codigo principal                                                            #
##########################################################################################################################################

import sys
import subprocess

suma=0
argumentosValidos = ['-m', '-o', '-r', '-n', '-O', '-i', '-e']
verificacionMOR=("-m", "-o", "-r")
argumentosIngresados=sys.argv[1::]

print('Argumentos ingresados', argumentosIngresados)
print()

print("Cantidad de parametros ingresados", len(argumentosIngresados))
print()

# Verifico la cantidad de parametros ingresados
if len(argumentosIngresados) > 10:
    
    cantidadDeParametrosIncorrectos()
    sys.exit(25)

else:

    # Verifico si se solicito ayuda
    for a in argumentosIngresados:
        if a == "-h":
            #Despliego el menu de ayuda
            ayuda()
            sys.exit()

    # Verifico que sean modificadores validos
    for b in argumentosIngresados:
        if b != argumentosValidos:
            parametrosIncorrectos()
            sys.exit(25)

    # Valido los parametros
    for x in argumentosIngresados:      # Recorre los modificadores
        for i in argumentosValidos:
            
            # Verifico que los parametros ingresados son los posibles
            if x == i:

                print(argumentosIngresados)

                for j in argumentosIngresados:
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

