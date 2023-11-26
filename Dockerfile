FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=banco_blibli
ENV MYSQL_USER=usuario
ENV MYSQL_PASSWORD=senha

COPY ./script.sql /docker-entrypoint-initdb.d/./script.sql