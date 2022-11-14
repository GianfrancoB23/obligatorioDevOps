#!/usr/bin/env python3

import sys
import subprocess
import os

suma=0
modificadoresValidos = ['-m', '-o', '-r', '-n', '-O', '-i', '-e']
verificacionMOR=("-m", "-o", "-r")
modificadoresIngresados=sys.argv[1::]

# subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o >> /home/administrator/obligatorio/prueba.txt", shell=True, capture_output=True,text=True,)
# res=subprocess.run("/home/administrator/obligatorio/ejercicio1_bash/ej1_archivos_y_cantidades.sh -m -o >> /home/administrator/obligatorio/prueba.txt", shell=True, capture_output=True,text=True,)
# print(res.stdout)
# print(res.stderr)

# modificadoresIngresados=sys.argv[1::]

# for i in modificadoresIngresados:
#     path=i

#     if os.path.exists(path) == True:

#         if os.access(path, os.R_OK) and os.access(path, os.X_OK) == True:
            
#             print("Existe el directorio")
#             os.chdir(path)
#             print('Estoy en', path)
#             # Ejecutar el codigo para que lo haga desde esa ubicacion, ubicacion dada por usuario.
#             # los primeros 3 parametros estan entre MOR, verificamos desde el 4to parametro hasta el 8vo
#             # si se le pasaron mas parametros ademas de mor tiene que pasarlo a un archivo y trabjar con ese
#             sys.exit()
#         else: 
#             print('No tiene los permisos necesarios')
#             sys.exit()

#     else:
#         print('No existe')
#         # Codigo para que evalue si son parametros validos y si no tengo una Ubicacion dada.
#         # si se le pasaron mas parametros ademas de mor tiene que pasarlo a un archivo y trabjar con ese.
#         sys.exit()


modificadoresIngresados=sys.argv[1::]
verificacionUbicacion = 0

for i in modificadoresIngresados:
    path=i
    
    if len(path) > 3: 
        verificacionUbicacion += 1
        ubicacion=path
    else:
        verificacionUbicacion += 0
    
if verificacionUbicacion == 1:

    if os.path.exists(ubicacion) == True:

        if os.access(ubicacion, os.R_OK) and os.access(ubicacion, os.X_OK) == True:
            
            print()
            print("Existe el directorio")
            os.chdir(ubicacion)
            print('Estoy en', ubicacion)
            print()
            # Ejecutar el codigo para que lo haga desde esa ubicacion, ubicacion dada por usuario.
            # los primeros 3 parametros estan entre MOR, verificamos desde el 4to parametro hasta el 8vo
            # si se le pasaron mas parametros ademas de mor tiene que pasarlo a un archivo y trabjar con ese
            sys.exit()
        else: 
            print('No tiene los permisos necesarios')
            # Mensaje que no se tienen los permisos necesarios
            sys.exit()

    else:
        print('No existe')
        # Mensaje de que el directorio no existe
        sys.exit()

else: 
    print('Evaluo sin direccion')
    print()
    # Evaluo sin direcion

