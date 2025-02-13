# Django E-Commmerce

## Virtual Environment

### Initial Virtual Environment
```shell
virtualenv venv
```

### Activate
```shell
source ./venv/Scripts/activate
```

### Deactivate
deactivate

## Initial Django Project
```shell
django-admin startproject $NAME_PROJECT
```
run app
```shell
cd $NAME_PROJECT
python manage.py runserver
```

## Database

Make migration

```shell
python manage.py makemigrations
```

Run migration

```shell
python manage.py migrate
```

## admin
create admin
``` shell
python manage.py createsuperuser
```