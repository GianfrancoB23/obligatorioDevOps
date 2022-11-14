#!/bin/bash

##########################################################################################################################################
#                                                  Variables generales del codigo                                                        #
##########################################################################################################################################

ultimo_parametro=${@: -1}   # El ultimo parametro cargado lo guarda en una variable

##########################################################################################################################################
#                                                   Funciones de filtros                                                                 #
##########################################################################################################################################

# Lista con filtros desde PWD
function lista-MOR-NOUbicacion () {
    find $PWD -type f 
}

# Lista con filtros desde /ubi
function lista-MOR-CONUbicacion () {
    find $ultimo_parametro -type f
}

# Lista sin filtros desde /ubi
function lista-SinFiltros-CONUbicacion () {
    directorio=$1
    find $directorio -mount -type f -not -path '*/\.*'
}

# Lista sin parametros desde PWD
function lista-SinFiltros-NOUbicacion () {
    find $PWD -mount -type f -not -path '*/\.*'
}

# Lista con -m desde PWD
function lista-m-NOUbicacion () {
    find $PWD -type f -not -path '*/\.*'
}

# Lista con -m desde /ubi 
function lista-m-CONUbicacion () {
    find $ultimo_parametro -type f -not -path '*/\.*'
}

# Lista con -o desde PWD
function lista-o-NOUbicacion () {
    find $PWD -mount -type f
}

# Lista con -o desde /ubi 
function lista-o-CONUbicacion () {
    find $ultimo_parametro -mount -type f
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
    find $ultimo_parametro -type f
}

# Lista con MO desde PWD
function lista-MO-NOUbicacion () {
    find $PWD -type f
}

# Lista con MR desde /ubi
function lista-MR-CONUbicacion () {
    find $ultimo_parametro -type f
}

# Lista con MR desde PWD
function lista-MR-NOUbicacion () {
    find $PWD -type f
}

# Lista con OR con /ubi
function lista-OR-CONUbicacion () {
    find $ultimo_parametro -mount -type f
}

# Lista con OR desde PWD
function lista-OR-NOUbicacion () {
    find $PWD -mount -type f
}


##########################################################################################################################################
#                                                            Codigo principal                                                            #
##########################################################################################################################################


if [ $# -gt 4 ]; then   # Evalua que la cantidad de parametros ingresados no sea mayor a 4, dado que en el caso mas completo se utiliza -m -o -r y una ubicacion
    
    echo 'Cantidad de parámetros incorrecta, solo se aceptan los modificadores -m, -o, -r y un directorio valido donde buscar los archivos'
    exit 4

else             # Evalua los parametros ingresado y ejecuta segun lo que suceda


    if [ $# = 4 ]; then # Evalua si son 4 parametros, puede ser MOR /UBI
        
        if [ -d $ultimo_parametro ]; then # Evalua si es un directorio
            
            if [ -r $ultimo_parametro ] && [ -x $ultimo_parametro ]; then     # Evalua si el ultimo parametro ingresado tiene permisos para leer y ejecutar ese directorio ingresado

                case ${@:1:3} in #Posibles casos que pueden suceder
                    '-m -o -r')
                        lista-MOR-CONUbicacion
                        echo ''
                        directorio=$ultimo_parametro
                        count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 1 - MOR"
                        echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                        echo '-------------------------------'
                    ;;
                    *) # Si no matchea con ningun flag, me tira mensaje de error
                        echo 'Modificador' $1,$2,$3 'inaceptable. Solo se aceptan -m, -o y -r y en ese orden.'
                    ;;
                esac

            else
                # Si no se tien los permisos necesarios
                echo 'No se tienen los permisos necesarios para acceder al directorio' $(realpath $ultimo_parametro) 'y poder desplegar el listado y sus cantidades.'
                exit 3
            fi
            
        elif [ -f $ultimo_parametro ]; then # Evaluo si es un archivo

            echo 'El directorio' $(realpath $ultimo_parametro) 'no es del tipo correcto.'
            exit 2

        else # Si el directorio no existe en el sistema

            echo 'El directorio' $(realpath $ultimo_parametro) 'no existe en este sistema.'
            exit 1

        fi

    elif [ $# = 3 ]; then # Opciones con 3 parametros, MOR sin ubicacion || MO - MR - OR con ubicacion

        if [ ${#ultimo_parametro} -le 3 ]; then # Evaluo si el ultimo parametro es un flag o una ubi, porque en caso que no pusieramos esto y pusieramos todo junto sin este if, evalua 2 veces en caso que se ponga un flag el cual lo evaluaria como ruta.
        
            case $@ in # Evaluo las posibilidades

                '-m -o -r')
                    lista-MOR-NOUbicacion
                    echo ''
                    count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                    if [ $count -gt 0 ]; then
                        echo "Cantidad de archivos listados:" $count
                    else
                        echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                        exit 0
                    fi
                    echo ''
                    echo "Opcion 2 - SIN UBI MOR"
                    echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
                    echo '-------------------------------'
                ;;
                *) # si no matchea con ningun parametro de los ingresados
                    echo 'Modificador' $1,$2,$3 'inaceptable. Solo se aceptan -m, -o y -r y en ese orden.'
                    ;;
            esac

        elif [ -d $ultimo_parametro ]; then
            if [ -r $ultimo_parametro ] && [ -x $ultimo_parametro ]; then 
                case ${@:1:2} in
                    '-m -o')
                        lista-MO-CONUbicacion
                        echo ''
                        directorio=$ultimo_parametro
                        count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 1 - MO"
                        echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                        echo $ultimo_parametro
                        echo '-------------------------------'
                    ;;
                    '-m -r')
                        lista-MR-CONUbicacion
                        echo ''
                        directorio=$ultimo_parametro
                        count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 2 - MR"
                        echo $ultimo_parametro
                        echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                        echo '-------------------------------'
                    ;;
                    '-o -r')
                        lista-OR-CONUbicacion
                        echo ''
                        directorio=$ultimo_parametro
                        count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 3 - OR"
                        echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                        echo '-------------------------------'
                    ;;
                    *)
                        echo 'Modificador' $1,$2,$3 'inaceptable. Solo se aceptan -m, -o y -r y en ese orden.'
                    ;;
                esac
            else
                # Si no se tien los permisos necesarios
                echo 'No se tienen los permisos necesarios para acceder al directorio' $(realpath $ultimo_parametro) 'y poder desplegar el listado y sus cantidades.'
                exit 3
            fi

        elif [ -f $ultimo_parametro ]; then

            echo 'El directorio' $(realpath $ultimo_parametro) 'no es del tipo correcto.'
            exit 2
        else 
            echo 'El directorio' $(realpath $ultimo_parametro) 'no existe en este sistema.'
            exit 1
        fi

    elif [ $# = 2 ]; then # Opcion 2 Parametros (Parametro -m / -o / -r + Ubicacion)   
        
        if [ ${#ultimo_parametro} -le 3 ]; then # Evaluo si el ultimo parametro es un flag o una ubi, porque en caso que no pusieramos esto y pusieramos todo junto sin este if, evalua 2 veces en caso que se ponga un flag el cual lo evaluaria como ruta.

                case ${@:1:2} in
                    '-m -o')
                        lista-MO-NOUbicacion
                        echo ''
                        count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos en el directorio " $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 1 - MO - sin ubicacion"
                        echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                        echo '-------------------------------'
                    ;;
                    '-m -r')
                        lista-MR-NOUbicacion
                        echo ''
                        count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos en el directorio " $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 2 - MR - sin ubicacion"
                        echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                        echo '-------------------------------'
                    ;;
                    '-o -r')
                        lista-OR-NOUbicacion
                        echo ''
                        count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 3 - OR - sin ubicacion"
                        echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                        echo '-------------------------------'
                    ;;
                    *)
                        echo 'Modificador' $1,$2,$3 'inaceptable. Solo se aceptan -m, -o y -r y en ese orden.'
                    ;;
                esac

        elif [ -d $ultimo_parametro ]; then
            if [ -r $ultimo_parametro ] && [ -x $ultimo_parametro ]; then
                case ${@:1:1} in
                    '-m')
                        lista-m-CONUbicacion
                        echo ''
                        directorio=$ultimo_parametro
                        count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos en el directorio " $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 1 - m"
                        echo "Parametro1"$1,"Parametro2"$2
                        echo '-------------------------------'
                    ;;
                    '-o')
                        lista-o-CONUbicacion
                        echo ''
                        directorio=$ultimo_parametro
                        count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 2 - o"
                        echo "Parametro1"$1,"Parametro2"$2
                        echo '-------------------------------'
                    ;;
                    '-r')
                        lista-r-CONUbicacion
                        echo ''
                        directorio=$ultimo_parametro
                        count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                        if [ $count -gt 0 ]; then
                            echo "Cantidad de archivos listados:" $count
                        else
                            echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                            exit 0
                        fi
                        echo ''
                        echo "Opcion 3 - r"
                        echo "Parametro1"$1,"Parametro2"$2
                        echo '-------------------------------'
                    ;;
                    *)
                        echo 'Modificador' $1 $2 $3 'inaceptable. Solo se aceptan -m, -o y -r y en ese orden.'
                    ;;
                esac
            else
                # Si no se tien los permisos necesarios
                echo 'No se tienen los permisos necesarios para acceder al directorio' $(realpath $ultimo_parametro) 'y poder desplegar el listado y sus cantidades.'
                exit 3
            fi

        elif [ -f $ultimo_parametro ]; then
        
            echo 'El directorio' $(realpath $ultimo_parametro) 'no es del tipo correcto.'
            exit 2
        else 
            echo 'El directorio' $(realpath $ultimo_parametro) 'no existe en este sistema.'
            exit 1
        fi

    elif [ $# = 1 ]; then # Un parametro -m / -o / -r SIN UBICACION

        if [ ${#ultimo_parametro} -le 3 ]; then # Evaluo si el ultimo parametro es un flag o una ubi, porque en caso que no pusieramos esto y pusieramos todo junto sin este if, evalua 2 veces en caso que se ponga un flag el cual lo evaluaria como ruta.
            
            case ${@:1:1} in
                '-m')
                    lista-m-NOUbicacion
                    echo ''
                    count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                    if [ $count -gt 0 ]; then
                        echo "Cantidad de archivos listados:" $count
                    else
                        echo "No se han encontrado archivos en el directorio " $(realpath $PWD)
                        exit 0
                    fi
                    echo ''
                    echo "Opcion 1 - m - SIN UBICACION"
                    echo "Parametro1"$1,"Parametro2"$2
                    echo '-------------------------------'
                ;;
                '-o')
                    lista-o-NOUbicacion
                    echo ''
                    count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                    if [ $count -gt 0 ]; then
                        echo "Cantidad de archivos listados:" $count
                    else
                        echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                        exit 0
                    fi
                    echo ''
                    echo "Opcion 2 - o - SIN UBICACION"
                    echo "Parametro1"$1,"Parametro2"$2
                    echo '-------------------------------'
                ;;
                '-r')
                    lista-r-NOUbicacion
                    echo ''
                    count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                    if [ $count -gt 0 ]; then
                        echo "Cantidad de archivos listados:" $count
                    else
                        echo "No se han encontrado archivos “comunes y corrientes”, ni siquiera ocultos, en el directorio" $(realpath $PWD)
                        exit 0
                    fi
                    echo ''
                    echo "Opcion 3 - r - SIN UBICACION"
                    echo "Parametro1"$1,"Parametro2"$2
                    echo '-------------------------------'
                ;;
                *)
                    echo 'Modificador' $1 $2 $3 'inaceptable. Solo se aceptan -m, -o y -r y en ese orden.'
                ;;
            esac
        
        elif [ -d $ultimo_parametro ]; then
            if [ -r $ultimo_parametro ] && [ -x $ultimo_parametro ]; then
                
                lista-SinFiltros-CONUbicacion $ultimo_parametro
                echo ''
                directorio=$ultimo_parametro
                count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
                if [ $count -gt 0 ]; then
                    echo "Cantidad de archivos listados:" $count
                else
                    echo "No se han encontrado archivos en el directorio" $(realpath $PWD)
                    exit 0
                fi
                echo ''
                echo "Opcion 1 - SIN FILTRO SOLO /UBI"
                echo "Parametro1"$1,"Parametro2"$2,"Parametro3"$3
                echo '-------------------------------'

            else
                # Si no se tien los permisos necesarios
                echo 'No se tienen los permisos necesarios para acceder al directorio' $(realpath $ultimo_parametro) 'y poder desplegar el listado y sus cantidades.'
                exit 3
            fi

        elif [ -f $ultimo_parametro ]; then
        
            echo 'El directorio' $(realpath $ultimo_parametro) 'no es del tipo correcto.'
            exit 2
        else 
            echo 'El directorio' $(realpath $ultimo_parametro) 'no existe en este sistema.'
            exit 1
        fi 

    else 
        lista-SinFiltros-NOUbicacion
        echo ''
        count=$(find $PWD -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
        if [ $count -gt 0 ]; then
            echo "Cantidad de archivos listados:" $count
        else
            echo "No se han encontrado archivos en el directorio " $(realpath $PWD)
            exit 0
        fi
        echo ''
        echo "Opcion 1 - SIN UBI SIN FILTRO"
        echo 'Opcion 1'$1,'Opcion 2'$2,'Opcion 3'$3
        echo '-------------------------------'
    fi
fi