# Utiliser l'image officielle Python 3.9 comme image de base
FROM python:3.12

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le répertoire de travail
COPY . .

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Lancer l'application Flask
CMD ["flask", "run"]
