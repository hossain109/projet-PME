# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY scripts/ ./scripts/

# Installer les dépendances
RUN pip install -r requirements.txt

EXPOSE 5000
#ENTRYPOINT : ["tail", "-f", "/dev/null"]
# Commande par défaut (exécuter un script "hello-world")
CMD ["python3", "scripts/hello-world.py"]
