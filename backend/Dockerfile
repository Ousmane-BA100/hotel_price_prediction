# Utiliser une image Python officielle
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential cmake ninja-build python3-dev ca-certificates && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires
COPY backend_api.py requirements.txt model/ tests/ /app/

# Définir PYTHONPATH pour que les tests puissent trouver backend_api.py
ENV PYTHONPATH=/app

# Mettre à jour pip et installer les dépendances Python
RUN pip install --no-cache-dir --trusted-host pypi.org \
    --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org \
    --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000 pour l'API Flask
EXPOSE 5000

# Définir la commande de démarrage du conteneur
CMD ["python", "backend_api.py"]
