# VENV
- comando para activar el virtualenv ***source rr_venv/Scripts/activate***
- comando para salir ***deactivate***
# RUNSERVER
- comando para correr el servidor y el proyecto ***python manage.py runserver***
  
# FOR operationlError no such table: auth user

- comando: 
  - python manage.py makemigrations
  - python manage.py migrate

# Models DB
- cree el modelo de la clase recetas

# Docker
https://www.youtube.com/watch?v=BoM-7VMdo7s
para correr la imagen creada
docker run -d -p 8000:8000 django-docker:0.0.1

# Deploying
https://www.youtube.com/watch?v=HPgAUObZ644&t=929s

leer los comentarios:

HOW TO SOLVE STATIC FILES NOT SHOWING:

Step 1:run pip install whitenoise

step 2: run  pip freeze > requirements.txt

step 3: In middleware in your settings.py file, add this line below the first middle: 
"whitenoise.middleware.WhiteNoiseMiddleware",

step 4: Configure static files. make sure you have something like this: 

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

step 5: Add this line to your settings.py file: 

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

step 6: run python manage.py collectstatic

step 7: push to github and try to redeploy

That should solve the issue