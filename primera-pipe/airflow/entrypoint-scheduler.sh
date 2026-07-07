#!/usr/bin/env bash
set -e

# Migra el metastore (idempotente: se puede correr en cada arranque).
airflow db migrate

# Crea el usuario admin de la UI si todavia no existe.
airflow users create \
    --username "${_AIRFLOW_WWW_USER_USERNAME}" \
    --password "${_AIRFLOW_WWW_USER_PASSWORD}" \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email "${_AIRFLOW_WWW_USER_EMAIL}" || true

# 'docker run --env-file' (a diferencia del 'env_file:' de compose) no
# soporta comentarios de fin de linea: genera una copia sin comentarios ni
# lineas vacias para que las tareas (BashOperator + docker run) la usen.
awk '{ sub(/[ \t]*#.*/, ""); if (length($0) > 0) print }' /opt/airflow/project.env > /opt/airflow/project.clean.env

# Marca listo para que el webserver (que depende de este healthcheck) arranque.
touch /opt/airflow/.initialized

exec airflow scheduler
