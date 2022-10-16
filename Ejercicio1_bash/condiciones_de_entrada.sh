#!/bin/bash 

# Verfica que la cantidad de parametros ingresados sean de 4 o menos, de lo contrario dira codigo de error


                        #     # Evalua MOR con ubicacion
                        # if [ $1='-m' ] & [ $2='-o' ] & [ $3='-r' ] & [ -d $4 ]; then
                            
                        #     lista-conFiltro-CONUbicacion
                        #     echo ''
                        #     contar_archivos $4
                        #     echo ''
                        #     echo "Opcion 1"
                        # fi

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
                    fi
                else
                    # No tiene permisos de ejecucion
                    
                fi