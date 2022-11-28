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

### Ejercicio 1:

- En el directorio del ejercicio 1 solamente se encuentra "ej1_archivos_y_cantidades.sh". 

Este puede ser corrido de las siguiente formas.

    $ ./ej1_archivos_y_cantidades.sh [-m] [-o] [-r] [ubicacion]

Ejemplo de salida si se ejecutara correctamente.

    $ ./ej1_archivos_y_cantidades.sh -m -o -r /home/administrator/obligatorio/ 

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/bash/ej1_sinError.gif?raw=true)

    $ ./ej1_archivos_y_cantidades.sh -m -o -r  

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/bash/ej1_sinErrorSinUbi.gif?raw=true)

Algo que se destaca, es que tiene que ser ejecutado en ese orden los flags, pudiendo o no estar alguno, pero no podria ser ejecutado lo siguiente:

    $ ./ej1_archivos_y_cantidades.sh -r /home/administrator/obligatorio/ -m
    
![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/bash/ej1_sinErrorModifUbi.gif?raw=true)

Error sin permisos.

    $ ./ej1_archivos_y_cantidades.sh -m -o -r /home/administrator/sinPermisosParaPrueba/

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/bash/ej1_errorSinPermisos.gif?raw=true)

Error de ubicacion invalida.

    $ ./ej1_archivos_y_cantidades.sh -m -o -r /home/administrator/obligatorix/ 

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/bash/ej1_errorUbi.gif?raw=true)

Error de directorio ingresado vacio.

    $ ./ej1_archivos_y_cantidades.sh -m -o -r /home/administrator/vacioParaPruebas/

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/bash/ej1_errorVacio.gif?raw=true)


### Ejercicio 2:

- Directorio del ejercicio /home/administrator/obligatorio/ejercicio2_python/
- Aca se encuentran ademas del codigo principal, archivos, en donde se segmento el codigo para facilitar la lectura de como funcionan los modificadores. 
- Tambien, se encuentra un script de bash, el cual sera utilizado para eliminar el archivo auxiliar creado para ejecutar las acciones que se le indiquen segun los modificadores.
- A diferencia del primer ejercicio, en este es posible ingresar los parametros en cualquier orden.
- En este ejercicio, existen diferentes combinaciones al momento de ingresar modificadores. En caso que se ingrese mas de un modificador que ordena, es decir, "-O {a,c,l}", tomaremos en cuenta el ultimo ingresado. Se deja una tabla a continuacion para entender cuales se ejecutaran. 

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/Posibilidades.jpg?raw=true)

Ejemplo de salida si se ejecutara correctamente.

    $ ./ej2_archivos_y_cantidades_exp.py -m -o -r -n -Ol -i

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/sinubicacion.gif?raw=true)

Se solicita ayuda.

- Puede ser llamada la -h sola o con otros parametros, pero si esta presente solamente ejecutara -h

    $ ./ej2_archivos_y_cantidades_exp.py -h

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/ayuda.gif?raw=true)

Ejemplo de salida si se indicara una expresion regular.

    $ ./ej2_archivos_y_cantidades_exp.py -m -o -r -n -Ol -i -e test /home/administrator/obligatorio/ejercicio2_python

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/expresionregular.gif?raw=true)

Ejemplo de salida si se indicara -Oc.

    $ ./ej2_archivos_y_cantidades_exp.py -m -o -r -n -Oc /home/administrator/obligatorio/ejercicio2_python

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/oc.gif?raw=true)

Ejemplo de salida si se indicara -Ol.

    $ ./ej2_archivos_y_cantidades_exp.py -m -o -r -n -Ol /home/administrator/obligatorio/ejercicio2_python

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/ol.gif?raw=true)

Ubicacion invalida.

    $ ./ej2_archivos_y_cantidades_exp.py -m -o -r /home/administrator/obligatorio/fghj -n

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/ubicacionInvalida.gif?raw=true)

Parametro repetido.

    $./ej2_archivos_y_cantidades_exp.py -m -o -r -n -Ol -Ol /home/administrator/obligatorio/ejercicio2_python/

![Animation](https://github.com/GianfrancoB23/obligatorioDevOps/blob/main/gifs/python/parametroRepetido.gif?raw=true)
