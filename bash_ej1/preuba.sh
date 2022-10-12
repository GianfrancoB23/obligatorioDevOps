#!/bin/bash

# find $1 -type f -not -path '*/\.*'

function listar () {
    directorio=$*
    find $directorio -type f -not -path '*/\.*'
}

function contar_archivos () {
    
    directorio=$*
    count=$(find $directorio -type f -not -path '*/\.*' | wc -l)
    echo "Cantidad de archivos listados:" $count
}

listar $1
echo ''
contar_archivos $1
echo ''

# Por defecto va a ejecutarse asi, dado que esto hace que no busque en el filesystem montado. 
function lista-DEFECTO-DIRECTORIO () {
    directorio=$*
    find $directorio -mount -type f -not -path '*/\.*'
}

# Lista sin parametros desde donde esta parado 
function lista-DEFECTO-PWD () {
    find . -mount -type f -not -path '*/\.*'
}

function listar(){
    #Si recibe tales parametros hace tales cosas
}