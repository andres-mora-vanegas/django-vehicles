# proyecto administración de vehículos con django

creación del ambiente virtual de python3

```sh
virtualenv -p python3 envname
```
# How to migrate Django from SQLite to PostgreSQL

## Dump existing data:

```sh
python3 manage.py dumpdata > datadump.json
```
## Change settings.py to Postgres backend.

## Make sure you can connect on PostgreSQL. Then:

```sh
python3 manage.py migrate --run-syncdb
```
## Run this on Django shell to exclude contentype data

```sh
python3 manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
Finally:
```

```sh
python3 manage.py loaddata datadump.json
```

## Despliegue de versión para heroku

```sh
git push heroku master
```

## ingreso al bash de heroku

```sh
heroku run bash
```
