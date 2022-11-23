# Obligatorio - Taller de Servidores Linux Matutino - 2022
## Docentes: Enrique Verdes - Sebastian Orrego
| ![LinuxLogo](https://github.com/heberdar/TSL/blob/main/images/Linux_logo.jpg) | ![RockyLogo](https://github.com/heberdar/TSL/blob/main/images/rocky-linux.jpg) |
| ----------- | ----------- |
## Recomendaciones generales

1. Se crean dos equipos uno con Rocky Linux 8.5 y uno con Ubuntu Server 22.04.
2. Se agregan dos tarjetas de Red una en Modo NAT y otra en Modo Virtual Host Only
3. Recordar que para continuar con la instalacion en UBUNTU es necesario desactivar la red.
4. Se particionan los discos con el siguiente diagrama LVM.


| Tamaño | Ubicación | 
| ----------- | ----------- |
| 1GB | /home |
| 1GB | /boot |
| 2GB | /SWAP|
| 5GB | /var |
| 5GB | /opt |
| 5GB | /    |
|![Ejemplo_Rocky8.5](https://github.com/heberdar/OBL_TSL/blob/main/images/rocky8_LVM.JPG) | ![Ejemplo_Ubuntu22.04](https://github.com/heberdar/OBL_TSL/blob/main/images/ubuntu_LVM.JPG) |

5. Se crea el usuario **ansible** en ambos equipos
6. Permisos sin tipeo de contraseña con el siguiente comando escriba **sudo visudo**

![sudo_visudo](https://github.com/heberdar/OBL_TSL/blob/main/images/sudo_visudo.jpg)

## Configuración del Bastión Rocky


#
# Desarrollo del código 

## Generalidades


## Roles

![sudo_visudo](https://github.com/heberdar/OBL_TSL/blob/main/images/Arbol.jpg)


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



### 3. Rol: createDatabase

Se crea la base de datos con el módulo **"mysql_db"**. Discriminamos según sistema operativo, ya que el socket de conexión se encuentra ubicado en diferentes rutas.



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
