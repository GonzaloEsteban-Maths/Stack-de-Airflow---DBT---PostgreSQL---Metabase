-- Se ejecuta SOLO la primera vez que se inicializa el volumen de datos.
CREATE SCHEMA IF NOT EXISTS raw;
COMMENT ON SCHEMA raw IS 'Capa raw: datos ingeridos tal cual, sin transformar';
