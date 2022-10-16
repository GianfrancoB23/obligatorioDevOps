#!/bin/bash

# Me lista los archivos de forma recursiva del directorio que le pase como parametro
function lista-SinFiltros-CONUbicacion () {
    directorio=$1
    find $directorio -type f -not -path '*/\.*'
}

# Lista sin parametros desde donde esta parado 
function lista-SinFiltros-NOUbicacion () {
    find $PWD -mount -type f -not -path '*/\.*'
}

# Me cuenta los archivos listados en el directorio pasado como parametro
function contar_archivos () {
    directorio=$*
    count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
    echo "Cantidad de archivos listados:" $count
}

palabra="$1"
primerCaracter=${palabra::1}

if [ -d $1 ] & [ $primerCaracter ]; then 

    lista-SinFiltros-CONUbicacion $1
    echo ''
    contar_archivos $1
    echo ''

fi

if [ -z $1 ]; then
    
    lista-SinFiltros-NOUbicacion
    echo ''
    contar_archivos $PWD
    echo ''

fi
