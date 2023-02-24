# Haelu Task

## Introduction and set up

I have provided a django instance intended to be used with postgres. 

The first step is to ***create an .env file*** to hold the value of the postgres password:

```bash
POSTGRES_PASSWORD=ASuperSecurePassword
```

The apps are containerised, so you can run the following:

```bash
docker compose build
docker compose -f docker-compose.yaml up
```

This will create two containers named backend and database. 

Alternatively, if you prefer a local install of python/django, there is an option just to build a test postgres db

```bash
docker compose -f docker-compose-pg.yaml up
```

Which will create a container called test-db and forward localhost:5432. If you choose this approach, you'll have to modify your django settings file, but I've left commentary near the DATABASES dictionary.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'haelu',
        'USER': 'haelu',
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'database',  # This is the host name of the docker db container as referenced inside of the backend container
        # 'HOST': 'localhost', # Use this host if you're running a containerised db with a local running django, e.g. for testing
        'PORT': 5432,
    }
}
```

There are some tests available that can be run with the following commands, depending on whether you're running locally or in containerised mode.

Containerised:
```bash
docker exec -it backend bash -c "pytest"
```

Local:
```bash
pytest
```
