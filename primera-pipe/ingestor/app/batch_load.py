from app.config import BATCH_ROWS
from app.db import get_connection, ensure_schema, insertar_ventas, contar_ventas
from app.generator import generar_venta


def main():
    conn = get_connection()
    ensure_schema(conn)

    ventas = [generar_venta(historico=False) for _ in range(BATCH_ROWS)]
    insertar_ventas(conn, ventas)

    print(f"[batch_load] +{BATCH_ROWS} filas insertadas | total raw.ventas = {contar_ventas(conn)}")
    conn.close()


if __name__ == "__main__":
    main()
