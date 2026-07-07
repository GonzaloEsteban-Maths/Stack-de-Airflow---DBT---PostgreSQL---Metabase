FROM python:3.12-slim

WORKDIR /usr/app

ENV PYTHONUNBUFFERED=1 \
    DBT_PROFILES_DIR=/usr/app/profiles

RUN pip install --no-cache-dir --retries 10 --timeout 120 \
    dbt-core==1.8.8 \
    dbt-postgres==1.8.2

COPY profiles.yml /usr/app/profiles/profiles.yml
COPY dbt_project/ /usr/app/dbt_project/

WORKDIR /usr/app/dbt_project

EXPOSE 8080

# Comando por defecto: servir la documentacion (UI persistente).
# Los jobs (dbt build, dbt docs generate, dbt test...) se lanzan bajo demanda:
#   docker compose run --rm dbt dbt build
#   docker compose run --rm dbt dbt docs generate
# (esto es exactamente lo que hara Airflow contra la imagen 'ingesta-dbt')
CMD ["dbt", "docs", "serve", "--host", "0.0.0.0", "--port", "8080"]
