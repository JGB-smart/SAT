# Desplegar backend

## Crear entorno virtual
virtualenv -p $(which python3) env

## Levantar entorno virtual
. env/bin/activate

## Instalar dependencias
python -m pip install -r requirements.txt 

## Correr migraciones si hace falta
./manage.py migrate

## Cargar los fixtures
python manage.py loaddata fixtures/*.json

## Correr server localhost
./manage.py runserver

## Correr server fuera de localhost
 ./manage.py runserver 0.0.0.0:8000

# En caso de que se necesita exportar tablas principales
python -Xutf8 manage.py dumpdata auth.group  --indent 4 > fixtures/001_group.json
python -Xutf8 manage.py dumpdata auth.permission  --indent 4 > fixtures/002_permission.json
python -Xutf8 manage.py dumpdata auth.group_permissions  --indent 4 > fixtures/003_group_permissions.json
python -Xutf8 manage.py dumpdata auth.user  --indent 4 > fixtures/004_user.json
python -Xutf8 manage.py dumpdata tareas.status  --indent 4 > fixtures/005_status.json
python -Xutf8 manage.py dumpdata tareas.prioridad  --indent 4 > fixtures/006_prioridad.json