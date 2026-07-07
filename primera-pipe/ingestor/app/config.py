import os

DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "postgres"),
    "port": int(os.getenv("POSTGRES_PORT", "5432")),
    "dbname": os.getenv("POSTGRES_DB", "raw_db"),
    "user": os.getenv("POSTGRES_USER", "raw_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "raw_pass"),
}

INITIAL_ROWS = int(os.getenv("INITIAL_ROWS", "1000"))
BATCH_ROWS = int(os.getenv("BATCH_ROWS", "20"))
