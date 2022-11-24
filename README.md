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

## Generalidades

Ejercicio 1:

El mismo se desarrollo de la siguiente forma, se establece una variable que se va a utilizar a lo largo del ejercico, seguido de esto se encuentran las funciones que fueron creadas para 

Se crearon carpetas en donde se guarda cada codigo segun el ejercicio.
En el caso del ejercicio 2, se presentan tambien diferentes codigos para que sea mas sencillo el entender el funcionamiento de los modificadores de python.
Esos mismos estan ubicados segun si seria llamado el modificador o no.

Por ultimo, el ejercicio 2, hace uso de un script crean en bash para eliminar el archivo auxiliar con el que se trabajo.

- database_user: nombre del usuario de la base de datos.
- database_password: password del usuario de la base de datos.
- database_name: nombre de la base de datos.
- port_to_open: puerto TCP que se va a abrir en los firewall.

Se utiliza en el código la condicional **"when"** para distinguir la familia de sistema operativo (RedHat o Debian). 

## Archivos a utilizar en el repositorio. 

- app.propierties: Archivo de conexión a base de datos.
- creartablas.sql: Estructura de tablas para la base de datos.
- jre-8u321-linux-x64.tar.gz: Archivo comprimido de instalación de **"Java 1.8"**.
- todo.war: Aplicación a desplegar.
- tomcat.service: Servicio de tomcat para el sistema operativo. 
- tomcat.tar.gz: Archivo comprimido de instalación de **"TomCat"**.

## Roles

![sudo_visudo](https://github.com/heberdar/OBL_TSL/blob/main/images/Arbol.jpg)

- Creamos el código principal llamado **"codigo.yaml"** y los siguientes roles:
1. "updateOS"
2. "installMariaDB"
3. "createDatabase"
4. "createUserDB"
5. "openPorts"

### 1. Rol: updateOS

Actualiza el sistema operativo según su familia (Debian o RedHat).

     - name: Update Ubuntu 
       apt:
         update_cache: yes
       when: ansible_facts['os_family'] == "Debian" 

      - name: Update Rocky
        yum:
          update_cache: yes
        when: ansible_facts['os_family'] == "RedHat"

### 2. Rol: installMariaDB

Se instala **"MariaDB"** y el complemento **"Python"** utilizado para la ejecución del moódulo **"mysql_db"** de Ansible. Además, en el caso de **Rocky**, dejamos el "enabled" e iniciamos el servicio. Ya que el sistema operativo no lo hace automáticamente como **"Ubuntu"**. 

    - name: Install MariaDB and python complement on Ubuntu
      apt:
        name: 
          - mariadb-server
          - python3-pymysql
        state: latest
      when: ansible_facts['os_family'] == "Debian"

    - name: Install MariaDB and python complement on Rocky
      package:
        name: 
          - mariadb-server
          - python3
        state: latest
      changed_when: true
      when: ansible_facts['os_family'] == "RedHat"

    - name: start mariadb
      systemd:
        name: mariadb
        enabled: yes
        state: started
      when: ansible_facts['os_family'] == "RedHat"
      
    - name:  Install pymysql on Rocky
      become: true
      pip: 
        name: pymysql
        state: present
      when: ansible_facts['os_family'] == "RedHat"

### 3. Rol: createDatabase

Se crea la base de datos con el módulo **"mysql_db"**. Discriminamos según sistema operativo, ya que el socket de conexión se encuentra ubicado en diferentes rutas.

    - name: Create Database "{{ database_name }}" on Ubuntu
      mysql_db:
        login_unix_socket: /var/run/mysqld/mysqld.sock
        name: "{{ database_name }}"
        state: present
      when: ansible_facts['os_family'] == "Debian"
    
    - name: Create Database "{{ database_name }}" on Rocky
      mysql_db:
        login_unix_socket: /var/lib/mysql/mysql.sock
        name: "{{ database_name }}"
        state: present
      when: ansible_facts['os_family'] == "RedHat"

### 4. Rol: createUserDB

Creación del usuario para la base de datos y asignación de permisos sobre la base de datos creada.

    - name: Create database user, named "{{ database_user }}" with all privileges over database "{{ database_name }}"
      mysql_user:
        login_unix_socket: /var/run/mysqld/mysqld.sock
        name: "{{ database_user }}"
        password: "{{ database_password }}"
        priv: "{{ database_name }}.*:ALL"
        state: present
      when: ansible_facts['os_family'] == "Debian"

    - name: Create database user, named "{{ database_user }}" with all privileges over database "{{ database_name }}"
      mysql_user:
        login_unix_socket: /var/lib/mysql/mysql.sock
        name: "{{ database_user }}"
        password: "{{ database_password }}"
        priv: "{{ database_name }}.*:ALL"
        state: present
      when: ansible_facts['os_family'] == "RedHat"

### 5. Rol: openPorts

Abre el puerto definido en el firewall. En el caso de **"Rocky"**, se hace un **"reload"** del servicio **"firewalld"** con un **"handler"**.

    - name: Permit traffic to port "{{ port_to_open }}" on Ubuntu
      ufw:
        rule: allow
        port: "{{ port_to_open }}"
      when: ansible_facts['os_family'] == "Debian"

    - name: Permit traffic to port "{{ port_to_open }}" on Rocky
      firewalld:
        port: "{{ port_to_open }}/tcp"
        permanent: yes
        state: enabled
      changed_when: true
      when: ansible_facts['os_family'] == "RedHat"
      notify: "firewalld reload"

Handler del rol: 

    ---
    - name: firewalld reload
      systemd:
        name: firewalld
        state: reloaded
        daemon_reload: true


## Playbook.

### Inicio de playbook.

Iniciamos el playbook, indicamos los host y cargamos variables.

    ---
    - name: Install appservers
      hosts: appservers
      vars:
        database_user: ort
        database_password: dariogianedgardo
        database_name: tallerlinux
        port_to_open: 8080
      become: yes

### Roles.

Invocamos los roles.

      roles: 
        - updateOS
        - openPorts
        - installMariaDB
        - createDatabase
        - createUserDB

### Tareas.

1. Creamos el directorio donde se va a encontrar **"Java 1.8"**.
2. Descomprimimos el archivo **"jre-8u321-linux-x64.tar.gz"**, que se encuentra en el repositorio a la carpeta creada anteriormente. 
3. Cargamos la variable de entorno con la ruta nueva de **"Java 1.8"**. 

        tasks:
        - name: Create directory for Java 1.8 
          file:
            path: /usr/java
            state: directory

        - name: Extract Java 1.8
          unarchive:
            src: ./files/jre-8u321-linux-x64.tar.gz
            dest: /usr/java
        
        - name: Export variable Java 
          command: echo 'export PATH="$PATH:/usr/java/jre1.8.0_321/bin"' >> ~/.bashrc && source ~/.bashr

4. Copia el archivo **"creartablas.sql"** que se encuentra en el repositorio, a la maquina remota. 
5. Crea las tablas en la base de datos a partir del archivo cargado anteriormente. 

        - name: Copy creartablas.sql to remote
          become: true 
          copy: 
            src: ./files/creartablas.sql
            dest: /home/ansible/
            owner: ansible
            group: ansible
            mode: 0744

        - name: Create tables SQL 
          mysql_db: 
            name: "{{ database_name }}" 
            state: import 
            target: /home/ansible/creartablas.sql
            login_user: "{{ database_user }}"
            login_password: "{{ database_password }}"

6. Crea el usuario y el grupo **"tomcat"**.
7. Extrae **"tomcat.tar.gz"** desde el repositorio a la ruta **"/opt/"**.
8. Se renombra la carpeta luego de la extración. 
9. Se le asignan los permisos y se cambia el **"ownership"** de la carpeta **"/opt/tomcat"**.

        - name: Create a Tomcat User and Group
          user:
            name: tomcat

        - name: Extract Tomcat
          unarchive:
            src: ./files/tomcat.tar.gz
            dest: /opt/
            owner: tomcat
            group: tomcat
            mode: 0755

        - name: Rename tomcat folder after to Extract
          command: mv /opt/apache-tomcat-9.0.65 /opt/tomcat

        - name: Change ownership of tomcat directory
          file:
            path: /opt/tomcat
            owner: tomcat
            group: tomcat
            mode: "u+rwx,g+rx,o=rx"
            recurse: yes
            state: directory
 
10. Creación del directorio **"/opt/config"**, donde va a estar ubicado el archivo de conexión a la base de datos. 
11. Copia el archivo **"app.properties"** que se encuentra en el repositorio, al directorio creado anteriormente y se le asignan los permisos. 

        - name: Create a /opt/config directory
          file:
            path: /opt/config
            owner: tomcat
            group: tomcat
            mode: 755
            recurse: yes

        - name: Copy app.properties to remote
          become: true 
          copy: 
            src: ./files/app.properties
            dest: /opt/config
            owner: tomcat
            group: tomcat
            mode: 0755

12. Copia el archivo **"tomcat.service"** que se encuentra en el repositorio, a la carpeta **"tomcat.service"** y se le asignan los permisos. 
13. Copia el archivo de configuración **"todo.war"** a **"/opt/tomcat/webapps/"** para hacer el despliegue de la aplicacion, con ciertos privilegios.
14. Se ejecuta el handler de reinicio para el proceso **"tomcat"** con el modulo **"systemd"**

        - name: Copy tomcat.service to remote
          become: true 
          copy: 
            src: ./files/tomcat.service
            dest: /etc/systemd/system/
            owner: tomcat
            group: tomcat
            mode: 0755
          changed_when: true
          notify: start tomcat
      
        - name: Copy todo.war to remote
          become: true 
          copy: 
            src: ./files/todo.war
            dest: /opt/tomcat/webapps/
            owner: tomcat
            group: tomcat
            mode: 0644

        handlers:
        - name: start tomcat
          systemd:
            name: tomcat
            state: started
            daemon_reload: true
#

## Ejecución

1. Posicionarse en la carpeta del repositorio **"OBL_TSL"** .
2. Editar el archivo **"appservers.ini"** agregando los host correspondientes
3. 
        [appservers]
        servidor1 ansible_host=XXX.YYY.ZZZ.WWW ansible_user=User
        servidor2 ansible_host=XXX.YYY.ZZZ.WWW ansible_user=User

4. Ejecutar la siguente linea de comando ansible-playbook codigo.yaml -i hosts/appservers.ini

### Demostración del funcionamiento

![Animation](https://github.com/heberdar/OBL_TSL/blob/main/images/Animation.gif)
