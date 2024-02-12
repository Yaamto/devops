# Utiliser une image de base Node.js
FROM node:18

# Créer un répertoire de travail dans l'image
WORKDIR /usr/src/app

# Installer Newman globalement dans l'image
RUN npm install -g newman

# Copier votre collection Postman et, si nécessaire, votre fichier d'environnement dans le répertoire de travail
COPY ./collections/iterator-test-nrg.json ./collections/iterator-test-nrg.json
# Décommentez la ligne suivante si vous avez un fichier d'environnement
COPY ./environments/int.postman_environment.json ./environments/int.postman_environment.json


CMD ["newman", "run", "collections/iterator-test-nrg.json", "-e", "environments/int.postman_environment.json"]
