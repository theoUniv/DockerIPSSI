FROM python:alpine3.10

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt d'abord pour tirer parti du cache Docker
COPY src/ /app/
COPY conf/requirements.txt .

# Installer les dépendances Python sans garder le cache

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade mysql-connector-python
RUN pip install -U flask werkzeug

# Exposer le port interne de l'application
EXPOSE 4743

# Commande par défaut pour démarrer l'application
CMD ["python", "app.py"]
