#!/bin/bash

############################# Verificar las condiciones sin ubicacion ###########################

# Lista con filtros desde PWD
function lista-conFiltro-NOUbicacion () {
    find $PWD -type f
}

# Lista con filtros desde /ubi
function lista-conFiltro-CONUbicacion () {
    find $i -type f
}

# Lista sin filtros desde /ubi
function lista-SinFiltros-CONUbicacion () {
    directorio=$1
    find $directorio -mount -not -path '*/\.*'
}

# Lista sin parametros desde PWD
function lista-SinFiltros-NOUbicacion () {
    find $PWD -mount -not -path '*/\.*'
}

# Lista con -m desde PWD
function lista-m-NOUbicacion () {
    find $PWD -not -path '*/\.*'
}

# Lista con -m desde /ubi 
function lista-m-CONUbicacion () {
    find $i -not -path '*/\.*'
}

# Lista con -o desde PWD
function lista-o-NOUbicacion () {
    find $PWD -mount 
}

# Lista con -o desde /ubi 
function lista-o-CONUbicacion () {
    find $i -mount
}

# Lista con -r desde /ubi
function lista-r-CONUbicacion () {
    directorio=$1
    find $directorio -mount -type f -not -path '*/\.*'
}

# Lista con -r desde PWD 
function lista-r-NOUbicacion () {
    find $PWD -mount -type f -not -path '*/\.*'
}

# Lista con MO desde /ubi
function lista-MO-CONUbicacion () {
    find $i
}

# Lista con MO desde PWD
function lista-MO-NOUbicacion () {
    find $PWD
}

# Lista con OR con /ubi
function lista-OR-CONUbicacion () {
    find $i -mount -type f
}

# Lista con OR desde PWD
function lista-OR-NOUbicacion () {
    find $PWD -mount -type f
}


# Me cuenta los archivos listados en el directorio pasado como parametro
function contar_archivos () {
    
    directorio=$*
    count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
    echo "Cantidad de archivos listados:" $count
}


# Verfica que la cantidad de parametros ingresados sean de 4 o menos, de lo contrario dira codigo de error
if [ $# -gt 4 ]; then
    echo 'Cantidad de parámetros incorrecta, solo se aceptan los modificadores -m, -o, -r y un directorio valido donde buscar los archivos'
    exit 4
else 

    # Verifica que la cantidad de parametros ingresados sea un ruta valida y lo carga en una variable.
    for i in $@; do
        
        if [ $i != "-m" ] && [ $i != "-o" ] && [ $i != "-r" ]; then
            
            if [ -d $i ]; then
                
                ruta=$(realpath $i)
                
                if [ -r $ruta ] && [ -x $ruta ]; then
                    
                    # Evalua los parametros ingresado y ejecuta segun lo que suceda

                    # Evalua MOR con ubicacion
                    if [ $1 == "-m" ] & [ $2 == "-o" ] & [ $3 == "-r" ]; then
                        
                        lista-conFiltro-CONUbicacion
                        echo ''
                        contar_archivos $i
                        echo ''
                        echo "Opcion 1"
                        echo '-------------------------------'
                        # Evalua MO con ubicacion
                    elif [ $1 == "-m" ] & [ $2 == "-o" ]; then
                        
                        lista-MO-CONUbicacion
                        echo ''
                        contar_archivos $i
                        echo ''
                        echo "Opcion 2"
                        echo '-------------------------------'
                        # Evalua OR con ubicacion
                    elif [ $1 == "-o" ] & [ $2 == "-r" ]; then
                        
                        lista-OR-CONUbicacion
                        echo ''
                        contar_archivos $i
                        echo ''
                        echo "Opcion 3"
                        echo '-------------------------------'
                        # Evalua M con ubicacion
                    elif [ $1 == "-m" ]; then
                        
                        lista-m-CONUbicacion
                        echo ''
                        contar_archivos $i
                        echo ''
                        echo "Opcion 4"
                        echo '-------------------------------'
                        # Evalua SIN PARAMETROS con ubicacion
                    elif [ $1 == "-o" ]; then
                        lista-o-CONUbicacion
                        echo ''
                        contar_archivos $i
                        echo ''
                        echo "Opcion 5"
                        echo '-------------------------------'
                    elif [ $1 == "-r" ]; then
                        lista-r-CONUbicacion
                        echo ''
                        contar_archivos $i
                        echo ''
                        echo "Opcion 6"
                        echo '-------------------------------'
                    else
                        lista-SinFiltros-CONUbicacion $i
                        echo ''
                        contar_archivos $i
                        echo ''
                        echo "Opcion 7"
                        echo '-------------------------------'
                    fi

                else
                    # ¡¡¡¡¡¡¡¡CORREGIR!!!!!!!!!! realpath tiene que completar /home/administrator/xx no /administrator
                    echo 'No se tienen los permisos necesarios para acceder al directorio' $(realpath $i) 'y poder desplegar el listado y sus cantidades.'
                fi

            else # Si el parametro no es un directorio:
                echo 'El directorio' $(realpath $i) 'no existe en este sistema.'
                exit 1
            fi
        fi
    done
fi

if [ -d ${@: -1} ]; then
  echo 'entro por positivo'
else
    if [ $1!="-m" ] && [ $2!="-o" ] && [ $3!="-r" ]; then
        
        if [ $1!="-m" ] && [ $2!="-o" ]; then

            if [ $1!="-o" ] && [ $2!="-r" ]; then

                if [ $1!="-m" ]; then

                    lista-SinFiltros-NOUbicacion
                    echo ''
                    contar_archivos $PWD
                    echo ''
                    echo "Opcion 8 - SIN UBI SIN FILTRO"
                    echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
                    echo '-------------------------------'

                else
                    lista-m-NOUbicacion
                    echo ''
                    contar_archivos $PWD
                    echo ''
                    echo "Opcion 6 - SIN UBI M"
                    echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
                    echo '-------------------------------'
                fi

            else
                lista-OR-NOUbicacion
                echo ''
                contar_archivos $PWD
                echo ''
                echo "Opcion 4 - SIN UBI OR"
                echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
                echo '-------------------------------'
            fi

        else    
            lista-MO-NOUbicacion
            echo ''
            contar_archivos $PWD
            echo ''
            echo "Opcion 3 - SIN UBI MO"
            echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
            echo '-------------------------------'
        fi

    else
        lista-conFiltro-NOUbicacion
        echo ''
        contar_archivos $PWD
        echo ''
        echo "Opcion 1 - SIN UBI MOR"
        echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
        echo '-------------------------------'
    fi
fi

# if [ $# -lt 4 ]; then
#     if [ $1!="-m" ] && [ $2!="-o" ] && [ $3!="-r" ]; then
        
#         if [ $1!="-m" ] && [ $2!="-o" ]; then

#             if [ $1!="-o" ] && [ $2!="-r" ]; then

#                 if [ $1 != "-m" ]; then

#                     lista-SinFiltros-NOUbicacion
#                     echo ''
#                     contar_archivos $PWD
#                     echo ''
#                     echo "Opcion 8 - SIN UBI SIN FILTRO"
#                     echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
#                     echo '-------------------------------'

#                 else
#                     lista-m-NOUbicacion
#                     echo ''
#                     contar_archivos $PWD
#                     echo ''
#                     echo "Opcion 6 - SIN UBI M"
#                     echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
#                     echo '-------------------------------'
#                 fi

#             else
#                 lista-OR-NOUbicacion
#                 echo ''
#                 contar_archivos $PWD
#                 echo ''
#                 echo "Opcion 4 - SIN UBI OR"
#                 echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
#                 echo '-------------------------------'
#             fi

#         else    
#             lista-MO-NOUbicacion
#             echo ''
#             contar_archivos $PWD
#             echo ''
#             echo "Opcion 3 - SIN UBI MO"
#             echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
#             echo '-------------------------------'
#         fi

#     else
#         lista-conFiltro-NOUbicacion
#         echo ''
#         contar_archivos $PWD
#         echo ''
#         echo "Opcion 1 - SIN UBI MOR"
#         echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
#         echo '-------------------------------'
#     fi
# fi
###################################################################
