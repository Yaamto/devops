##Utiliser une image MySQL officielle en tant qu'image de base
FROM mysql:latest

##Informations de mainteneur
LABEL maintainer="Hallouli <hallouli@email.com>"

##Variables d'environnement pour configurer MySQL
ENV MYSQL_ROOT_PASSWORD=root_password \
    MYSQL_DATABASE=my_database \
    MYSQL_USER=db_user \
    MYSQL_PASSWORD=db_password

##Copier les scripts d'initialisation dans le conteneur
COPY ./scripts/ /docker-entrypoint-initdb.d/

##Exposer le port MySQL
EXPOSE 3306