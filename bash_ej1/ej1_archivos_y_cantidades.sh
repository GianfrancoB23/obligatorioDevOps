#!/bin/bash

# Lista con filtros desde donde esta parado
function lista-conFiltro-NOUbicacion () {
    find $PWD -type f
}

# Lista con filtros con ubicacion
function lista-conFiltro-CONUbicacion () {
    find $4 -type f
}

# Lista sin filtros con ubicacion
function lista-SinFiltros-CONUbicacion () {
    directorio=$1
    find $directorio -mount -not -path '*/\.*'
}

# Lista sin parametros desde donde esta parado
function lista-SinFiltros-NOUbicacion () {
    find $PWD -mount -not -path '*/\.*'
}



# Lista con -m desde donde esta parado 
function lista-m-NOUbicacion () {
    find $PWD -not -path '*/\.*'
}

# Lista con -m y con ubicacion 
function lista-m-CONUbicacion () {
    find $2 -not -path '*/\.*'
}

# Lista con -o desde donde esta parado 
function lista-o-NOUbicacion () {
    find $PWD -mount 
}

# Lista con -o desde una ubicacion 
function lista-o-NOUbicacion () {
    find $2 -mount 
}

# Lista con MO desde una ubicacion
function lista-MO-CONUbicacion () {
    find $3
}

# Lista con MO desde donde esta parado
function lista-MO-CONUbicacion () {
    find $PWD
}

# Lista con OR desde donde esta parado
function lista-OR-CONUbicacion () {
    find $PWD -mount -type f
}

# Lista con OR desde una ubicacion
function lista-OR-CONUbicacion () {
    find $3 -mount -type f
}

# Me cuenta los archivos listados en el directorio pasado como parametro
function contar_archivos () {
    
    directorio=$*
    count=$(find $directorio -type f | wc -l) #Esta funcion cuenta los archivos ocultos y no ocultos desde la ruta que se ingreso
    echo "Cantidad de archivos listados:" $count
}

# Evalua si tiene parametros ingresados
    ## Hacer que tenga parametros ingresados

# Evalua los parametros ingresado y ejecuta segun lo que suceda

# Evalua MOR con ubicacion
if [ $1='-m' ] & [ $2='-o' ] & [ $3='-r' ] & [ -d $4 ]; then
    
    lista-conFiltro-CONUbicacion
    echo ''
    contar_archivos $4
    echo ''
    echo "Opcion 1"
fi

# Evalua MOR sin ubicacion
if [ $1='-m' ] & [ $2='-o' ] & [ $3='-r' ] & [ -z $4 ]; then
    
    lista-conFiltro-NOUbicacion
    echo ''
    contar_archivos $PWD
    echo ''
    echo "Opcion 2"
fi

# Evalua MO con ubicacion
if [ $1='-m' ] & [ $2='-o' ] & [ -d $3 ]; then
    
    lista-MO-CONUbicacion
    echo ''
    contar_archivos $3
    echo ''
    echo "Opcion 3"
fi

# Evalua OR con ubicacion
if [ $1='-o' ] & [ $2='-R' ] & [ -d $3 ]; then
    
    lista-OR-CONUbicacion
    echo ''
    contar_archivos $PWD
    echo ''
    echo "Opcion 4"
fi

# Evalua OR sin ubicacion
if [ $1='-o' ] & [ $2='-r' ] & [ -z $3 ]; then 
    
    lista-OR-NOUbicacion
    echo ''
    contar_archivos $PWD
    echo ''
    echo "Opcion 5"
fi

# Evalua M con ubicacion
if [ $1='-m' ] & [ -d $2 ]; then
    
    lista-m-CONUbicacion
    echo ''
    contar_archivos $2
    echo ''
    echo "Opcion 6"
fi

# Evalua M sin ubicacion
if [ $1='-m' ] & [ -z $2 ]; then

    lista-m-NOUbicacion
    echo ''
    contar_archivos $PWD
    echo ''
    echo "Opcion 7"
fi

# Evalua SIN PARAMETROS con ubicacion
if [ -d $1 ]; then

    lista-SinFiltros-CONUbicacion $1
    echo ''
    contar_archivos $1
    echo ''
    echo "Opcion 8"
fi

# Evalua SIN parametros y SIN ubicacion
if [ -z $1 ]; then

    lista-SinFiltros-NoUbicacion
    echo ''
    contar_archivos $PWD
    echo ''
    echo "Opcion 9"
fi
# find / -type f -not -path '*/\.*' --> me muestra los archivos de forma recursiva y no los archivos ocultos

#Validar si es un directorio
# '''
# if [ -d "$RUTA" ]; then
#     echo "La ruta: $RUTA recibida es un directorio"
# '''