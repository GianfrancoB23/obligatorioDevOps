#!/usr/bin/env python3
'''
                        NOTAS

- Cambiar la ubicacion de la variable fullpath a /tmp/aux antes de entregar
- Cambiar la ubicacion de la variable filename a lo largo del codigo por /tmp/ 

'''


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
fullpath='/home/administrator/obligatorio/ejercicio2_python/aux' #Full Path donde se ubica el archivo auxiliar Esto se tiene que cambiar por /TMP/aux al momento de entregar el OBL

##############################################################################################################################
#                                                  Codigo principal                                                          #
##############################################################################################################################

# Verifico la cantidad de parametros ingresados
if len(modificadoresIngresados) > 10:
    
    cantidadDeParametrosIncorrectos()
    sys.exit(25)

else:
    
    # Verifico si algun parametro es una ubicacion
    for i in modificadoresIngresados:
        path=i
        
        if len(path) > 3: 
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
                print("Existe el directorio")
                os.chdir(ubicacion) # Cambio la ubicacion a la ingresada para que se ejecute directamente en ese directorio
                print('Estoy ubicado en', ubicacion)

                # Verifico si se solicito ayuda
                for a in modificadoresIngresados:
                    if a == "-h":
                        #Despliego el menu de ayuda
                        ayuda()
                        sys.exit()

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

                    # En Aux, se debe escribir la ruta Absoluta a /tmp/
                    with open(fullpath,'w') as salida:
                        res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o -r", stdout=salida, shell=True,text=True,)

                        formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                        os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                        # Lo identifico
                        filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

                elif suma == 5:
                    print("MR")
                    ## MR ##

                    # En Aux, se debe escribir la ruta Absoluta a /tmp/
                    with open(fullpath,'w') as salida:
                        res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -r", stdout=salida, shell=True,text=True,)

                        formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                        os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                        # Lo identifico
                        filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

                elif suma == 4:
                    print("R")
                    ## R ##

                    # En Aux, se debe escribir la ruta Absoluta a /tmp/
                    with open(fullpath,'w') as salida:
                        res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -r", stdout=salida, shell=True,text=True,)

                        formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                        os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                        # Lo identifico
                        filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

                elif suma == 3:
                    print("MO")
                    ## MO ##

                    # En Aux, se debe escribir la ruta Absoluta a /tmp/
                    with open(fullpath,'w') as salida:
                        res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o", stdout=salida, shell=True,text=True,)

                        formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                        os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                        # Lo identifico
                        filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

                elif suma == 2:
                    print("O")
                    ## O ##

                    # En Aux, se debe escribir la ruta Absoluta a /tmp/
                    with open(fullpath,'w') as salida:
                        res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -o", stdout=salida, shell=True,text=True,)

                        formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                        os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                        # Lo identifico
                        filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

                elif suma == 1:
                    print("M")
                    ## M ##

                    # En Aux, se debe escribir la ruta Absoluta a /tmp/
                    with open(fullpath,'w') as salida:
                        res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m", stdout=salida, shell=True,text=True,)

                        formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                        os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                        # Lo identifico
                        filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

                elif suma == 0:
                    print("Sin parametros ingresados")
                    ## Sin parametros ##

                    # En Aux, se debe escribir la ruta Absoluta a /tmp/
                    with open(fullpath,'w') as salida:
                        res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh", stdout=salida, shell=True,text=True,)

                        formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                        os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                        # Lo identifico
                        filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

                # Assigno los valores correspondientes a los modificadores que se ingresaron
                for d in modificadoresIngresados:
                    if d == modificadoresPython[0]:
                        sumaModificadorPython+=1
                    elif d == modificadoresPython[1]:
                        sumaModificadorPython+=2
                    elif d == modificadoresPython[2]:
                        sumaModificadorPython+=4
                    elif d == modificadoresPython[3]:
                        sumaModificadorPython+=8                    
                    elif d == modificadoresPython[4]:
                        sumaModificadorPython+=16
                    elif d == modificadoresPython[5]:
                        sumaModificadorPython+=32

                # En caso que no se reciban modificadores de Python, debera mostrar el archivo por defecto tal como sale de shell
                if sumaModificadorPython==0:
                    with open(filename) as infile:
                        lines = infile.readlines()
                        for line in lines:
                            print(line)

                if sumaModificadorPython==57:
                    print('n Ol i e')
                    sys.exit()
                elif sumaModificadorPython==53:
                    print('n Oc i e')
                    sys.exit()
                elif sumaModificadorPython==51:
                    print('n Oa i e')
                    sys.exit()
                elif sumaModificadorPython==49:
                    print('n i e')
                    sys.exit()
                elif sumaModificadorPython==48:
                    print('i e')
                    sys.exit()
                elif sumaModificadorPython==33:
                    print('n e')
                    sys.exit()
                elif sumaModificadorPython==32:
                    print('e')
                    sys.exit()
                elif sumaModificadorPython==25:
                    print('n Ol i')
                    sys.exit()
                elif sumaModificadorPython==21:
                    print('n Oc i')
                    sys.exit()
                elif sumaModificadorPython==19:
                    print('n Oa i')
                    sys.exit()
                elif sumaModificadorPython==17:
                    print('n i')
                    sys.exit()
                elif sumaModificadorPython==16:
                    print('i')
                    sys.exit()
                elif sumaModificadorPython==9:
                    print('n Ol')
                    sys.exit()
                elif sumaModificadorPython==5:
                    print('n Oc')
                    sys.exit()
                elif sumaModificadorPython==3:
                    print('n Oa')
                    sys.exit()
                elif sumaModificadorPython==1:
                    print('n')
                    sys.exit()

                sys.exit()
            else: 
                print('No se tienen los permisos necesarios para acceder al directorio', ubicacion)
                sys.exit()

        else:
            print('El directorio',ubicacion,'no existe en este sistema.')
            sys.exit()

    else: 
        print('Evaluo sin direccion')
        print()
        
        # Verifico si se solicito ayuda
        for a in modificadoresIngresados:
            if a == "-h":
                #Despliego el menu de ayuda
                ayuda()
                sys.exit()

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

            # En Aux, se debe escribir la ruta Absoluta a /tmp/
            with open(fullpath,'w') as salida:
                res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o -r", stdout=salida, shell=True,text=True,)

                formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                # Lo identifico
                filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

        elif suma == 5:
            print("MR")
            ## MR ##

            # En Aux, se debe escribir la ruta Absoluta a /tmp/
            with open(fullpath,'w') as salida:
                res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -r", stdout=salida, shell=True,text=True,)

                formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                # Lo identifico
                filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

        elif suma == 4:
            print("R")
            ## R ##

            # En Aux, se debe escribir la ruta Absoluta a /tmp/
            with open(fullpath,'w') as salida:
                res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -r", stdout=salida, shell=True,text=True,)

                formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                # Lo identifico
                filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

        elif suma == 3:
            print("MO")
            ## MO ##

            # En Aux, se debe escribir la ruta Absoluta a /tmp/
            with open(fullpath,'w') as salida:
                res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o", stdout=salida, shell=True,text=True,)

                formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                # Lo identifico
                filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

        elif suma == 2:
            print("O")
            ## O ##

            # En Aux, se debe escribir la ruta Absoluta a /tmp/
            with open(fullpath,'w') as salida:
                res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -o", stdout=salida, shell=True,text=True,)

                formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                # Lo identifico
                filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

        elif suma == 1:
            print("M")
            ## M ##

            # En Aux, se debe escribir la ruta Absoluta a /tmp/
            with open(fullpath,'w') as salida:
                res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m", stdout=salida, shell=True,text=True,)

                formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                # Lo identifico
                filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

        elif suma == 0:
            print("Sin parametros ingresados")
            ## Sin parametros ##

            # En Aux, se debe escribir la ruta Absoluta a /tmp/
            with open(fullpath,'w') as salida:
                res = subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh", stdout=salida, shell=True,text=True,)

                formatoppid = '{}.tmp'.format(os.getppid()) #Definir PPID.tmp
                os.rename(fullpath, formatoppid) #Cambio de nombre del fullpath al formatonuevo

                # Lo identifico
                filename = '/home/administrator/obligatorio/ejercicio2_python/'+str(formatoppid)

        
        for d in modificadoresIngresados:
            if d == modificadoresPython[0]:
                sumaModificadorPython+=1
            elif d == modificadoresPython[1]:
                sumaModificadorPython+=2
            elif d == modificadoresPython[2]:
                sumaModificadorPython+=4
            elif d == modificadoresPython[3]:
                sumaModificadorPython+=8                    
            elif d == modificadoresPython[4]:
                sumaModificadorPython+=16
            elif d == modificadoresPython[5]:
                sumaModificadorPython+=32

        if sumaModificadorPython==57:
            print('n Ol i e')
            sys.exit()
        elif sumaModificadorPython==53:
            print('n Oc i e')
            sys.exit()
        elif sumaModificadorPython==51:
            print('n Oa i e')
            sys.exit()
        elif sumaModificadorPython==49:
            print('n i e')
            sys.exit()
        elif sumaModificadorPython==48:
            print('i e')
            sys.exit()
        elif sumaModificadorPython==33:
            print('n e')
            sys.exit()
        elif sumaModificadorPython==32:
            print('e')
            sys.exit()
        elif sumaModificadorPython==25:
            print('n Ol i')
            sys.exit()
        elif sumaModificadorPython==21:
            print('n Oc i')
            sys.exit()
        elif sumaModificadorPython==19:
            print('n Oa i')
            sys.exit()
        elif sumaModificadorPython==17:
            print('n i')
            sys.exit()
        elif sumaModificadorPython==16:
            print('i')
            sys.exit()
        elif sumaModificadorPython==9:
            print('n Ol')
            sys.exit()
        elif sumaModificadorPython==5:
            print('n Oc')
            sys.exit()
        elif sumaModificadorPython==3:
            print('n Oa')
            sys.exit()
        elif sumaModificadorPython==1:
            print('n')
            sys.exit()

        sys.exit()