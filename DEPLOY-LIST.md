### PASOS PARA DESPLIEGUE

    1.- Utilizar librería de variables de entorno ()
        `python-dotenv`

    2.- Configurar el settings para que lea el .env

    3.- Verificar que el proyecto sea versionado con git 
    (Github, Bitbucket, GitLab)
        3.1.- Comando para inicializar git
            git init (en el directorio del proyecto)
        3.2.- git add . (Agregar archivos actualizados)
        3.3.- git commmit -m "feat: mensaje"    
    4.- Crearse una cuenta y configurar la misma en cloud (digital, aws, azure)
    5.- Acceder mediante SSH al servidor con las credenciales.
    6.- Si es ubuntu ejecutar comando de actualización.
        apt-get update
        apt-get upgrade
    7.- Instalar gunicorn.
    8.- Definir ruta de proyecto /var/www
    9.- Clonarse el proyecto del repositorio de git
        git clone <url>
    10.- Instalar servidor web nginx.
    11.- Verificar mensaje de exito del servidor web.
    12.- Instalar en el servidor postgresql
    13.- Configurar bd.
    14.- Ingresar al shell de postgres
        sudo -u postgres psql
    15.- Creo bd a enlazar al aplicativo
        CREATE DATABASE cursodb;
    16.- Creo el usuario a gestionar la bd creada previamente
        CREATE USER <username> WITH PASSWORD '<clave>';
    17.- Darle permisos al usuario de gestionar la bd
         GRANT ALL PRIVILEGES ON DATABASE <db> TO <username>;
    18.- Salir del shell de postgres
        \q
    19.- Instalar environment.
        sudo apt-get install python3-venv
    20.- Crear un entorno virtual.
        python3 -m venv ./venv
    21.- Activar el entorno virtual.   
        source venv/bin/activate
    22.- Instalar dependencias del proyecto
        pip isntall -r requirements.txt
    23.- Comando para verificar si se instalaron las dependencias
        pip list
    24.- Crear el archivo .env con las configuraciones correspondientes (BD, Secret Key)
    25.- Crear gunicorn.socket
    26.- Crear gunicorn.server
    27.- Iniciar el service del gunicorn
    28.- Activar el gunicron.socket 
         sudo systemctl start gunicorn.socket
         sudo systemctl enable gunicorn.socket
    29.- Configuracion del nginx (servidor web)
    30.- Enlazar el sites-enabled del nginx.
        sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/
    31.- Reiniciar el servicio nginx.
        sudo systemctl restart nginx
    32. Revisar archivos estaticos de proyecto django.
        python manage.py collectstatic