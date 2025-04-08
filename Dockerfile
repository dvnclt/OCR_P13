# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exposer le port utilisé par Django
EXPOSE 8000

# Commande pour collecter les fichiers statiques et lancer Gunicorn
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]