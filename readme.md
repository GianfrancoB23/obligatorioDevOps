# Obligatorio - Programacion para DevOps Matutino - 2022
## Docentes: Federico Barceló - Agustín Nebril
## Alumnos: Gianfranco Bonanni (274029) - Dario Meneses (257370)

## RECOMENDACIONES

1. Ubicar los codigos en el siguiente path según ejercicio: 
     - Ejercicio 1: "/home/administrator/obligatorio/ejercicio1_bash/".
     - Ejercicio 2: "/home/administrator/obligatorio/ejercicio2_python"
     
     Este punto es realmente importante, debido a que en cierta parte del codigo, tiene paths hardcodeadas.
2. Otorgarle los permisos necesarios a los codigos. 

# Desarrollo del código 

### Generalidades

Ejercicio 1:

- En el directorio del ejercicio 1 solamente se encuentra "ej1_archivos_y_cantidades.sh". 

Este puede ser corrido de las siguiente formas.

    $ ./ej1_archivos_y_cantidades.sh [-m] [-o] [-r] [ubicacion]

Algo que se destaca, es que tiene que ser ejecutado en ese orden los flags, pudiendo o no estar alguno, pero no podria ser ejecutado lo siguiente:

    $ ./ej1_archivos_y_cantidades.sh -r /home/administrator/ -m

Ejemplos de salidas si se ejecutara correctamente.

    $ ./ej1_archivos_y_cantidades.sh -m -o -r /home/administrator/obligatorio/ 

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/bash/ej1_sinError.gif?raw=true)

