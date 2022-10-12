#!/bin/bash

ls s1 s2 s3 s4

s1 = ubicacion

s2 = opcion 1 de parametro [puede ser -m -r -o]
s3 = opcion 2 de parametro [puede ser -m -r -o]
s4 = opcion 3 de parametro [puede ser -m -r -o]


# La realidad de lo que esta ejecutando es 
find /admin/cosas -type f -recusive 

- m = -la #liste oculto
- r = -recursive #recursivo


# -m, -r, -o tienen que ser funciones

'''En los mensajes de error siempre la ruta que muestre va a tener que ser una ruta absoluta, por ejemplo, ingrese ./clase pero la ruta que me va a mostrar es /home/admin/clase'''
# esto lo hago almacenando la ruta en una variable 
'''
ruta = ./
ruta_absoluta = pwd
ruta_absoluta_final = ruta_absoluta + ruta
'''