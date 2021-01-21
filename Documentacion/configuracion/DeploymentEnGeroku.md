# Hacer deployment en Heroku con proyecto en Django 
## Primer Paso
1. Crear una cuenta gratuita en heroku
2. Instalar con el entorno virtual activado desde la terminal:
    pip install gunicorn        -Es el servidos http para Unix
3. Instalamos la libreria de gestion de la base de datos PostgresSql
    pip install psycopg2
 
4. Para conectar el proyecto con el gestor la base de datos PostgresSql utilizamos la libreria 
    pip install dj-database-url

5. Para inciar el servidor se usaran variables de entorno y para ello se utilizara la libreria
    pip install python-dacouple
6. Instalamos la libreria whitenoise para gestionar archivos estaticos ya que django en produccion no lo hace
    pip install whitenoise
    
7. Generar el archivo requirentes el cual tiene todas las librerias utilizadas en el proyecto
    pip freeze > requirements.txt
    * NOTA: Si agregamos nuevas librerias debemos actualizar el archivo requirements asi : pip freeze > requirements.txt
    
## Segunado Paso
###Modificar el archivo settings
1. Debug = False        --Para que no muestre los errores--
2. ALLOWED_HOSTS = ['*']    --Para este caso * indicando que se van a permitir todos los host o si no se coloca la url
3. Configurar la base de datos: se debe cambiar la configuracion actual por esta
    import dj_database_url
    from decouple import config
    DATABASES = {
        'default' : dj_database_url.config(
            default = config('DATABASE_URL')
        )
    }
3. Configurar los archivos estaticos agregamos
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

4. Agregamos en MIDDLEWARE
   * 'whitenoise.middleware.WhiteNoiseMiddleware',
    
5. Agregamos al final del settings lo siguiente
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
## Tercer Paso
###Modificar el archivo urls

1. Importamos estos dos paquetes cuando va a estar en heroku en el archivo urls
    * from django.conf import settings
    * from django.conf.urls.static import static
2. Luego, agregamos por fuera del corchete de urlpatterns
    * +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
## Cuarto Paso
###Crear la  carpeta  static 
Esta carpeta contiene todos los archivos estaticos utilizados en el proyecto y no puede esar vacia por que genera error.
1. si no esta se debe crear, esta debe estar al mismo nivel del manage.py

## Quinto Paso
###Crear el archivo Procfile
Este archivo se crea para que gunicorn ejecute el archivo wsgi del proyecto

1. Crear un archivo de tipo texto al mismo nivel del manage.py con el nombre Procfile y agregamos la siguiente linea
* web: gunicorn gestionacademica.wsgi --log-file-

    
## Sexto Paso
###Crear un commit de los cambios en git

1. Desde consola:
* git add --all
* git commit -m "Mensaje"

## Septimo Paso
###Crear un proyecto en Heroku: Se debe tener una cuenta activa
1. Instalar HerokuCli desde https://devcenter.heroku.com/articles/heroku-cli para poderlo utilizar desde la terminal
2. Loguerse desde la consola o terminal
* heroku login
* Iniciamos sesion en la pagina donde nos lanzo
3. Creamos el proyecto asi
* heroku create nombredelproyecto
4. Agregamos el repositorio de git a heroku
*heroku git:remote -a nombredelproyecto
5. Creamos la base de datos asi
* heroku addons:create heroku-postgresql:hobby-dev
6. Subimos el repositorio de git a keroku este proceso tarda segun el tamaño del proyecto
* git push heroku master 



    




    
