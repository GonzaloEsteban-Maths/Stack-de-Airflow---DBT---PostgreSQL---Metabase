-- Se ejecuta SOLO la primera vez que se inicializa el volumen de datos.
-- Base de datos separada para el metastore de Airflow (mismo usuario/host que raw_db).
CREATE DATABASE airflow_db;
COMMENT ON DATABASE airflow_db IS 'Metastore de Airflow (scheduler + webserver)';
