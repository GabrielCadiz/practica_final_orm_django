# Proyecto Final ORM en Django

Este proyecto es una aplicación web desarrollada con **Django** y **PostgreSQL**. Permite gestionar información de laboratorios, incluyendo su creación, edición y eliminación, utilizando vistas basadas en funciones.

---

## **Requisitos previos**

Asegúrate de tener instalados los siguientes componentes antes de comenzar:
- Python 3.8+
- Django 4.x
- PostgreSQL
- Virtualenv (opcional pero recomendado)

---

## **Instrucciones para configurar el proyecto**

### **1. Clonar el repositorio**
Clona este proyecto en tu máquina local:
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

Es recomendable usar un entorno virtual para instalar las dependencias:

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

Instala las librerías requeridas desde el archivo requirements.txt:

pip install -r requirements.txt

Crea una base de datos PostgreSQL y configura las credenciales en settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_final_orm',
        'USER': 'userdjango',
        'PASSWORD': 'userdjango',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Ejecuta las migraciones para crear las tablas necesarias:

python manage.py makemigrations
python manage.py migrate

Crea un superusuario para acceder al panel de administración de Django:

python manage.py createsuperuser

Ejecuta el servidor de desarrollo para comprobar que todo funciona correctamente:

python manage.py runserver

Accede al proyecto en http://127.0.0.1:8000

Este proyecto incluye pruebas unitarias para verificar:

La correcta inserción de datos en la base de datos.
Que las URL responden con un código HTTP 200.
Que las vistas usan las plantillas adecuadas.

Ejecuta las pruebas con el siguiente comando:

python manage.py test

Para restaurar un respaldo de la base de datos, usa:

pg_restore -U userdjango -d db_final_orm backup.sql

Autor: Gabriel Cadiz Echeverria










