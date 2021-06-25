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
    