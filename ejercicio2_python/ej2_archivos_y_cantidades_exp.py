#!/usr/bin/env python3

##############################################################################################################################
#                                                    Modulos                                                                 #
##############################################################################################################################

import sys
import subprocess
import os
import re

##############################################################################################################################
#                                                Variables y listas                                                          #
##############################################################################################################################

modificadoresValidos = ['-m', '-o', '-r', '-n', '-Oa', '-Oc', '-Ol', '-i', '-e'] # Verificadores validos en total
verificacionMOR=("-m", "-o", "-r") # Verificadores de MOR
suma=0 # Verificador para validar existencia de MOR
modificadoresPython = ['-n', '-Oa', '-Oc', '-Ol', '-i', '-e'] # Verificadores que validos del codigo de Python
sumaModificadorPython=0 # Verificador para validar existencia de modificadores de python
modificadoresIngresados=sys.argv[1::] # los parametros que se ingresaron, se excluye el primero ya que es el archivo
verificacionUbicacion = 0 # Verifica si se ingreso una ubicacion
error=0 # Valida que los parametros sean los correctos

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
    print("Modificadores inaceptables, solamente se aceptan una sola vez los siguientes:")
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
#                                                  Codigo principal                                                          #
##############################################################################################################################

# Verifico que los flags no hayan sido ingresados 2 veces
presente=0
for i in modificadoresIngresados:
    for x in modificadoresIngresados:
        if i == x:
            presente+=1
            
        else:
            presente+=0

        if presente > 1: 
            parametrosIncorrectos()
            sys.exit(25)
    presente=0

# Verifico si algun parametro es una ubicacion
num=0
for i in modificadoresIngresados:
    path=i
    num+=1
    anterior=num-1
    parametroAnteriorIngresado=sys.argv[anterior]

    # Comprueba si el parametro ingresado tiene un largo mayor a 3, porque si lo es puede ser una ruta, pero tambien verifica que el parametro anterior
    # no sea -e, porque en ese caso, podria ser una expresion regular.
    if len(path) > 3 and not parametroAnteriorIngresado == '-e':
        verificacionUbicacion += 1 # si existe un argumento que su largo sea mayor a 3 se convierte en 1
        ubicacion=path
    else:
        verificacionUbicacion += 0 # Si no existe un argumento que su largo sea mayor a 3, el verificador continua en 0
    
if verificacionUbicacion == 1: # Si hubo una ubicacion

    # Verifico que la ruta exista
    if os.path.exists(ubicacion) == True:

        # Verifico si tengo Lectura y escritura en ese directorio
        if os.access(ubicacion, os.R_OK) and os.access(ubicacion, os.X_OK) == True:
            
            # Ejecuto el codigo para los modificadores
            print("Existe el directorio y tengo permisos de ejecucion")

            # Verifico si se solicito ayuda
            for a in modificadoresIngresados:
                if a == "-h":
                    #Despliego el menu de ayuda
                    ayuda()
                    sys.exit(0)

            # Verifico que sean modificadores validos
            for b in modificadoresIngresados:
                for c in modificadoresValidos:
                    
                    # Como ya se que uno de los modificadores ingresados es una ubicacion, le resto 1 para que no me de error
                    if len(b)>3:
                        error=-1
                    # Si el valor ingresado es diferente de los valores validos sumara un error
                    if b != c:
                        error+=1
                    else:   # De lo contrario restara un error
                        error-=1
                
                if error == 7: # Si se encontro que uno de los valores es positivo, reseteara el contador de error para el siguiente parametro
                    error=0
            # Si el valor es mayor a 6, se sabe que no matcheo con ningun verificador valido
            if error > 8:                                   
                parametrosIncorrectos()
                sys.exit(25)

            print(modificadoresIngresados)

            for j in modificadoresIngresados:
                if j == verificacionMOR[0]:
                    suma = suma + 1
                elif j == verificacionMOR[1]:
                    suma = suma + 2
                elif j == verificacionMOR[2]:
                    suma = suma + 4

            if suma == 7: 
                print("MOR")
                ## MOR ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o -r " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)
                

            elif suma == 6:
                print("OR")
                ## MR ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -o -r " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

            elif suma == 5:
                print("MR")
                ## MR ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -r " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

            elif suma == 4:
                ## R ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -r " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

            elif suma == 3:
                print("MO")

                ## MO ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

            elif suma == 2:
                print("O")
                ## O ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -o " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)
                    
            elif suma == 1:
                print("M")
                ## M ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

            elif suma == 0:
                print("Sin modificador MOR")
                ## Sin modificadores ##
                #Nombre y ubicacion
                formatoppid = '{}.txt'.format(os.getppid())
                #print(formatoppid)

                filename='/tmp/'+str(formatoppid)

                with open(filename,'w') as salida:
                    ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh " + ubicacion
                    res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

            # Assigno los valores correspondientes a los modificadores que se ingresaron
            for d in modificadoresIngresados:
                if d == modificadoresPython[0]:
                    sumaModificadorPython+=32
                elif d == modificadoresPython[1]:
                    sumaModificadorPython+=16
                elif d == modificadoresPython[2]:
                    sumaModificadorPython+=8
                elif d == modificadoresPython[3]:
                    sumaModificadorPython+=4                    
                elif d == modificadoresPython[4]:
                    sumaModificadorPython+=2
                elif d == modificadoresPython[5]:
                    sumaModificadorPython+=1

            if sumaModificadorPython==63:
                print('Se ejecuta -n -Ol -i -e')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)
                
                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==62:
                print('-n -Ol -i')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==61:
                print('-n -Ol -e')

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


                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==60:
                print('-n -Ol')

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

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)
                
                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==59:
                print('-n -Oc -i -e')

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
                        
                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==58:
                print('-n -Oc -i')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==57:
                print('-n -Oc -e')

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

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==56:
                print('-n -Oc')

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

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==55:
                print('-n -Ol -i -e')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==54:
                print('-n -Ol -i')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==53:
                print('-n -Ol -e')

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


                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==52:
                print('-n -Ol')

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

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==51:
                print('-n -Oa -i -e')


                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==50:
                print('-n -Oa -i')

                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==49:
                print('-n -Oa -e')

                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==48:
                print('-n -Oa')

                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==47:
                print('-n -Ol -i -e')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==46:
                print('-n -Ol -i')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==45:
                print('-n -Ol -e')

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


                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==44:
                print('-n -Ol')

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

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)
                
                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==43:
                print('-n -Oc -i -e')

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
                        
                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==42:
                print('-n -Oc -i')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)
                
                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==41:
                print('-n -Oc -e')

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

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==40:
                print('-n -Oc')

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

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==39:
                print('-n -Ol -i -e')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==38:
                print('-n -Ol -i')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==37:
                print('-n -Ol -e')

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


                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==36:
                print('-n -Ol')

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

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==35:
                print('-n -i -e')

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==34:
                print('-n -i')

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==33:
                print('-n -e')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==32:
                print('-n')

                ######################################
                #               N
                ######################################

                #Imprimir Linea completa donde esta esa ocurrencia.
                filename = open(filename, 'r')
                for line in filename:
                    if not re.findall(r"^Cantidad de archivos listados:", line):
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==31:
                print('-Ol -i -e')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==30:
                print('-Ol -i')

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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==29:
                print('-Ol -e')

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

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==28:
                print('-Ol')

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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==27:
                print('-Oc -i -e')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==26:
                print('-Oc -i')

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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==25:
                print('-Oc -e')

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

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==24:
                print('-Oc')

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
                
                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==23:
                print('-Ol -i -e')

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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==22:
                print('-Ol -i')

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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==21:
                print('-Ol -e')
                
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

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==20:
                print('-Ol')

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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==19:
                print('-Oa -i -e')
                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==18:
                print('-Oa -i')
                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==17:
                print('-Oa -e')
                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==16:
                print('-Oa')
                #######################################
                #                Oa
                #######################################

                bands= list()

                with open (filename) as fin:
                    for line in fin:
                        bands.append(line.strip())

                bands.sort()

                with open(filename, 'w') as infile:
                    for number, band in enumerate(bands):
                        if number not in [0,1,2]:
                            infile.write(band + '\n')

                #######################################
                #       Imprime Oa
                #######################################

                with open(filename) as infile:
                    lines = infile.readlines()
                    for line in lines:
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==15:
                print('-Ol -i -e')
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
                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==14:
                print('-Ol -i')
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
                        
                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==13:
                print('-Ol -e')
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
                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==12:
                print('-Ol')
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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==11:
                print('-Oc -i -e')
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

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==10:
                print('-Oc -i')
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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==9:
                print('-Oc -e')
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

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==8:
                print('-Oc')
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
                        
                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==7:
                print('-Ol -i -e')
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
                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==6:
                print('-Ol -i')

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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==5:
                print('-Ol -e')
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
                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==4:
                print('-Ol')
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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit()
            elif sumaModificadorPython==3:
                print('-i -e')

                ##############################################
                #                i
                ##############################################

                # Invierto el archivo
                invertido=reversed(list(open(filename)))

                # Lo voy agregando linea por linea al archivo de forma ordenada
                with open(filename, 'w') as infile:
                    for line in invertido:
                        infile.write(line.rstrip() + '\n')

                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==2:
                ## i
                print("-i")
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

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==1:
                ## e
                print('-e')
                #############################################
                #                   e
                #############################################

                parametroIngresado=sys.argv[1::]

                encontro=0
                num=0
                for i in parametroIngresado:
                    expresionRegular=i
                    num+=1
                    anterior=num-1
                    parametroAnteriorIngresado=sys.argv[anterior]

                    if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                        filename = open(filename, 'r')
                        for line in filename:
                            if re.search(expresionRegular, line):
                                encontro+=1
                                coincidencia=line
                                print(coincidencia)
                            else:
                                encontro+=0

                if encontro <= 0:
                    print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
                    sys.exit(25)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            elif sumaModificadorPython==0:
                ## sin modificadores
                print('Sin modificadores de python')

                ##############################################
                #           Muestro el archivo sin cambios
                ##############################################

                with open(filename) as infile:
                    lines = infile.readlines()
                    for line in lines:
                        print(line)

                os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
                sys.exit(0)
            sys.exit(0)
        else: 
            print('No se tienen los permisos necesarios para acceder al directorio', ubicacion)
            sys.exit(3)

    else:
        print('El directorio',ubicacion,'no existe en este sistema.')
        sys.exit(1)

else: 
    print('Evaluo sin direccion')
    print()
    
    # Verifico si se solicito ayuda
    for a in modificadoresIngresados:
        if a == "-h":
            #Despliego el menu de ayuda
            ayuda()
            sys.exit(0)

    # Verifico que sean modificadores validos
    for b in modificadoresIngresados:
        for c in modificadoresValidos:
            
            # Como ya se que uno de los modificadores ingresados es una ubicacion, le resto 1 para que no me de error
            if len(b)>3:
                error=-1
            # Si el valor ingresado es diferente de los valores validos sumara un error
            if b != c:
                error+=1
            else:   # De lo contrario restara un error
                error-=1
        
        if error == 7: # Si se encontro que uno de los valores es positivo, reseteara el contador de error para el siguiente parametro
            error=0
    # Si el valor es mayor a 6, se sabe que no matcheo con ningun verificador valido
    if error > 8:                                   
        parametrosIncorrectos()
        sys.exit(25)

    print(modificadoresIngresados)

    for j in modificadoresIngresados:
        if j == verificacionMOR[0]:
            suma = suma + 1
        elif j == verificacionMOR[1]:
            suma = suma + 2
        elif j == verificacionMOR[2]:
            suma = suma + 4

    if suma == 7: 
        print("MOR")
        ## MOR ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o -r "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)
        

    elif suma == 6:
        print("OR")
        ## MR ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -o -r "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

    elif suma == 5:
        print("MR")
        ## MR ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -r "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

    elif suma == 4:
        ## R ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -r "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

    elif suma == 3:
        print("MO")

        ## MO ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

    elif suma == 2:
        print("O")
        ## O ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -o "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)
            
    elif suma == 1:
        print("M")
        ## M ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

    elif suma == 0:
        print("Sin modificador MOR")
        ## Sin modificadores ##
        #Nombre y ubicacion
        formatoppid = '{}.txt'.format(os.getppid())
        #print(formatoppid)

        filename='/tmp/'+str(formatoppid)

        with open(filename,'w') as salida:
            ejecucion="/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh "
            res = subprocess.run(ejecucion, stdout=salida, shell=True,text=True)

    # Assigno los valores correspondientes a los modificadores que se ingresaron
    for d in modificadoresIngresados:
        if d == modificadoresPython[0]:
            sumaModificadorPython+=32
        elif d == modificadoresPython[1]:
            sumaModificadorPython+=16
        elif d == modificadoresPython[2]:
            sumaModificadorPython+=8
        elif d == modificadoresPython[3]:
            sumaModificadorPython+=4                    
        elif d == modificadoresPython[4]:
            sumaModificadorPython+=2
        elif d == modificadoresPython[5]:
            sumaModificadorPython+=1

    if sumaModificadorPython==63:
        print('Se ejecuta -n -Ol -i -e')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        
        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==62:
        print('-n -Ol -i')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        # Abro el archivo para mostrarlo
        with open(filename) as infile:
            lines = infile.readlines()
            for line in lines:
                print(line)

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==61:
        print('-n -Ol -e')

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


        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)


        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==60:
        print('-n -Ol')

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

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)
        
        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==59:
        print('-n -Oc -i -e')

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
                
        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)


        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==58:
        print('-n -Oc -i')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==57:
        print('-n -Oc -e')

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

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==56:
        print('-n -Oc')

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

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==55:
        print('-n -Ol -i -e')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==54:
        print('-n -Ol -i')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        # Abro el archivo para mostrarlo
        with open(filename) as infile:
            lines = infile.readlines()
            for line in lines:
                print(line)

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==53:
        print('-n -Ol -e')

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


        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==52:
        print('-n -Ol')

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

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==51:
        print('-n -Oa -i -e')

        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==50:
        print('-n -Oa -i')

        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==49:
        print('-n -Oa -e')

        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==48:
        print('-n -Oa')

        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==47:
        print('-n -Ol -i -e')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==46:
        print('-n -Ol -i')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        # Abro el archivo para mostrarlo
        with open(filename) as infile:
            lines = infile.readlines()
            for line in lines:
                print(line)

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==45:
        print('-n -Ol -e')

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


        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==44:
        print('-n -Ol')

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

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)
        
        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==43:
        print('-n -Oc -i -e')

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
                
        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==42:
        print('-n -Oc -i')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)
        
        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==41:
        print('-n -Oc -e')

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

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==40:
        print('-n -Oc')

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

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==39:
        print('-n -Ol -i -e')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==38:
        print('-n -Ol -i')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        # Abro el archivo para mostrarlo
        with open(filename) as infile:
            lines = infile.readlines()
            for line in lines:
                print(line)

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==37:
        print('-n -Ol -e')

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


        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==36:
        print('-n -Ol')

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

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==35:
        print('-n -i -e')

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==34:
        print('-n -i')

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==33:
        print('-n -e')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==32:
        print('-n')

        ######################################
        #               N
        ######################################

        #Imprimir Linea completa donde esta esa ocurrencia.
        filename = open(filename, 'r')
        for line in filename:
            if not re.findall(r"^Cantidad de archivos listados:", line):
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==31:
        print('-Ol -i -e')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==30:
        print('-Ol -i')

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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==29:
        print('-Ol -e')

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

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==28:
        print('-Ol')

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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==27:
        print('-Oc -i -e')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==26:
        print('-Oc -i')

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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==25:
        print('-Oc -e')

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

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==24:
        print('-Oc')

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
        
        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==23:
        print('-Ol -i -e')

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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==22:
        print('-Ol -i')

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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==21:
        print('-Ol -e')
        
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

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==20:
        print('-Ol')

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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==19:
        print('-Oa -i -e')
        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==18:
        print('-Oa -i')
        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==17:
        print('-Oa -e')
        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==16:
        print('-Oa')
        #######################################
        #                Oa
        #######################################

        bands= list()

        with open (filename) as fin:
            for line in fin:
                bands.append(line.strip())

        bands.sort()

        with open(filename, 'w') as infile:
            for number, band in enumerate(bands):
                if number not in [0,1,2]:
                    infile.write(band + '\n')

        #######################################
        #       Imprime Oa
        #######################################

        with open(filename) as infile:
            lines = infile.readlines()
            for line in lines:
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==15:
        print('-Ol -i -e')
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
        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==14:
        print('-Ol -i')
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
                
        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==13:
        print('-Ol -e')
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
        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==12:
        print('-Ol')
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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==11:
        print('-Oc -i -e')
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

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==10:
        print('-Oc -i')
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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==9:
        print('-Oc -e')
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

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==8:
        print('-Oc')
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
                
        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==7:
        print('-Ol -i -e')
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
        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==6:
        print('-Ol -i')

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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==5:
        print('-Ol -e')
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
        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==4:
        print('-Ol')
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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit()
    elif sumaModificadorPython==3:
        print('-i -e')

        ##############################################
        #                i
        ##############################################

        # Invierto el archivo
        invertido=reversed(list(open(filename)))

        # Lo voy agregando linea por linea al archivo de forma ordenada
        with open(filename, 'w') as infile:
            for line in invertido:
                infile.write(line.rstrip() + '\n')

        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)


        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==2:
        ## i
        print("-i")
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

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==1:
        ## e
        print('-e')
        #############################################
        #                   e
        #############################################

        parametroIngresado=sys.argv[1::]

        encontro=0
        num=0
        for i in parametroIngresado:
            expresionRegular=i
            num+=1
            anterior=num-1
            parametroAnteriorIngresado=sys.argv[anterior]

            if len(expresionRegular) > 3 and parametroAnteriorIngresado == '-e':
                filename = open(filename, 'r')
                for line in filename:
                    if re.search(expresionRegular, line):
                        encontro+=1
                        coincidencia=line
                        print(coincidencia)
                    else:
                        encontro+=0

        if encontro <= 0:
            print('La expresion regular dada con el parámetro -e es incorrecta. Por favor, Ingrese una expresión regular bien formulada.')
            sys.exit(25)


        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    elif sumaModificadorPython==0:
        ## sin modificadores
        print('Sin modificadores de python')

        ##############################################
        #           Muestro el archivo sin cambios
        ##############################################

        with open(filename) as infile:
            lines = infile.readlines()
            for line in lines:
                print(line)

        os.system('/home/administrator/obligatorio/ejercicio2_python/borrar.sh > /dev/null 2>&1')
        sys.exit(0)
    sys.exit(0)