#!/bin/bash

# Charger le fichier .env
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Vérifie si DOCKER_USERNAME est défini
if [ -z "$DOCKER_USERNAME" ]; then
    echo "Error: DOCKER_USERNAME is not set. Please set it as an environment variable."
    exit 1
fi

# Variables
DOCKER_IMAGE="${DOCKER_USERNAME}/ocr_p13:${1:-latest}"  # Utilise le hash du commit ou "latest" par défaut
CONTAINER_NAME="ocr_p13_container"

# Récupérer l'image depuis Docker Hub
echo "Pulling Docker image: $DOCKER_IMAGE"
docker pull $DOCKER_IMAGE

# Supprimer tout conteneur existant avec le même nom
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping and removing existing container: $CONTAINER_NAME"
    docker rm -f $CONTAINER_NAME
fi

# Lancer le conteneur
echo "Running Docker container: $CONTAINER_NAME"
docker run -d -p 8000:8000 --name $CONTAINER_NAME $DOCKER_IMAGE

# Afficher le statut
echo "The site is running at http://localhost:8000"
