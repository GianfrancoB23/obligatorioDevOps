#!/bin/bash

palabra="$1"
primerCaracter=${palabra::1}

if [ $primerCaracter==/ ];then
    echo 'hola mundo'
else
    echo 'adios mundo'
fi
