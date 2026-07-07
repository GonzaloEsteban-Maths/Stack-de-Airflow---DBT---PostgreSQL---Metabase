-- Se ejecuta SOLO la primera vez que se inicializa el volumen de datos.
-- Base de datos separada para el metastore de Metabase (mismo usuario/host que raw_db).
CREATE DATABASE metabase_db;
COMMENT ON DATABASE metabase_db IS 'Metastore de Metabase (dashboards, usuarios, configuracion)';
