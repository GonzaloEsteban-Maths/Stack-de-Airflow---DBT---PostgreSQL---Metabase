import time

import psycopg2
from psycopg2.extras import execute_values

from app.config import DB_CONFIG


def get_connection(retries=15, delay=3):
    ultimo_error = None
    for intento in range(1, retries + 1):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.autocommit = False
            print("[db] Conexion con Postgres establecida.")
            return conn
        except psycopg2.OperationalError as e:
            ultimo_error = e
            print(f"[db] Postgres no disponible (intento {intento}/{retries}). Reintento en {delay}s...")
            time.sleep(delay)
    raise RuntimeError(f"No se pudo conectar a Postgres: {ultimo_error}")


def ensure_schema(conn):
    with conn.cursor() as cur:
        cur.execute("CREATE SCHEMA IF NOT EXISTS raw;")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS raw.ventas (
                id           BIGSERIAL     PRIMARY KEY,
                uuid         UUID          NOT NULL,
                cliente      TEXT          NOT NULL,
                email        TEXT          NOT NULL,
                producto     TEXT          NOT NULL,
                categoria    TEXT          NOT NULL,
                cantidad     INTEGER       NOT NULL,
                precio_unit  NUMERIC(10,2) NOT NULL,
                total        NUMERIC(12,2) NOT NULL,
                pais         TEXT          NOT NULL,
                creado_en    TIMESTAMPTZ   NOT NULL,
                ingerido_en  TIMESTAMPTZ   NOT NULL DEFAULT now()
            );
        """)
    conn.commit()


def contar_ventas(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT count(*) FROM raw.ventas;")
        return cur.fetchone()[0]


def insertar_ventas(conn, ventas):
    sql = """
        INSERT INTO raw.ventas
            (uuid, cliente, email, producto, categoria,
             cantidad, precio_unit, total, pais, creado_en)
        VALUES %s;
    """
    filas = [
        (v["uuid"], v["cliente"], v["email"], v["producto"], v["categoria"],
         v["cantidad"], v["precio_unit"], v["total"], v["pais"], v["creado_en"])
        for v in ventas
    ]
    with conn.cursor() as cur:
        execute_values(cur, sql, filas)
    conn.commit()
