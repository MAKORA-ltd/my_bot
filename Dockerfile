FROM python:3.8-slim-buster

WORKDIR /app

# Installation des paquets système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers du projet
COPY . .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Configuration des variables d'environnement
ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Commande de démarrage
CMD ["python3", "-m", "shivu"]
