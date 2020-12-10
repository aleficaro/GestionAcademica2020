# Para crear un entorno virual para un proyecto:

1. Instalar virtualenv

a) Abrir el cmd del sistema
b) pip install virtualenv
**********************************************
2. Crear entorno virtual para el proyecto

a) Desde el cmd entrar a la carpeta del proyecto
b) ejecutar el comando: virtualenv nombredelentornovirtual
***********************************************************

3. Instalar Django en el entorno virtual

a) Activar el entorno virtual asi:  cd proyecto\nombredelentornovirtual\scripts\activate
b) Con el entorno activado ejecutar: pip install Django
c) Con el mismo comando anterior se instalan las librerias necesarias en el entorno virtual
***********************************************************

4. Ejecutar el proyecto

a) Con el entorno activado: cd proyecto\nombre de la app\ python manage.py runserver
*******************************************************************************************
