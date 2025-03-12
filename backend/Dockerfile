# Utiliser l'image officielle Python
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY backend_api.py requirements.txt model/ /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask
EXPOSE 5000

# Commande pour exécuter Flask
CMD ["python", "backend_api.py"]
