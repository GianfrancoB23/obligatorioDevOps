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

suma=0
modificadoresValidos = ['-m', '-o', '-r', '-n', '-Oa', '-Oc', '-Ol', '-i', '-e']
modificadoresPython = ['-n', '-Oa', '-Oc', '-Ol', '-i', '-e']
verificacionMOR=("-m", "-o", "-r")
modificadoresIngresados=sys.argv[1::]

##############################################################################################################################
#                                                  Codigo principal                                                          #
##############################################################################################################################

# Verifico la cantidad de parametros ingresados
if len(modificadoresIngresados) > 10:
    
    cantidadDeParametrosIncorrectos()
    sys.exit(25)

else:

    for i in modificadoresIngresados:
        path=i

        if len(path) > 3: 
            verificacionUbicacion=1
        else:
            verificacionUbicacion=0
    
    if verificacionUbicacion==1:

        # Verifico que la ruta exista
        if os.path.exists(path) == True:

            # Verifico si tengo Lectura y escritura en ese directorio
            if os.access(path, os.R_OK) and os.access(path, os.X_OK) == True:
                
                print("Existe el directorio")
                os.chdir(path) # Cambio el directorio donde se trabaja
                # Ejecutar el codigo para que lo haga desde esa ubicacion, ubicacion dada por usuario.
                # los primeros 3 parametros estan entre MOR, verificamos desde el 4to parametro hasta el 8vo
                # si se le pasaron mas parametros ademas de mor tiene que pasarlo a un archivo y trabjar con ese

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

                        # Si el valor ingresado es diferente de los valores validos sumara un error
                        if b != c:
                            error+=1
                        else:   # De lo contrario restara un error
                            error-=1
                    if error == 7: # Si se encontro que uno de los valores es positivo, reseteara el contador de error para el siguiente parametro
                        error=0
                print("Esto es error al final",error)
                # Si el valor es mayor a 6, se sabe que no matcheo con ningun verificador valido
                if error > 8:                                   
                    parametrosIncorrectos()
                    sys.exit(25)

                # '-m', '-o', '-r', '-n', '-Oa', '-Oc', '-Ol', '-i', '-e'

                # Valido los parametros
                for x in modificadoresIngresados:      # Recorre los modificadores
                    for z in modificadoresValidos:
                        
                        # Verifico que los parametros ingresados son los posibles
                        if x == z:

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
                
                sys.exit()
            else: 
                print('No se tienen los permisos necesarios para acceder al directorio')
                sys.exit()

        else:
            print('No existe')
            # Mensaje de que el directorio no existe
            sys.exit()

    else: 
        print('Evaluo sin direccion')
        print()
        # Evaluo sin direcion