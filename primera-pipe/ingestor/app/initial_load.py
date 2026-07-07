from app.config import INITIAL_ROWS
from app.db import get_connection, ensure_schema, contar_ventas, insertar_ventas
from app.generator import generar_venta


def main():
    conn = get_connection()
    ensure_schema(conn)

    existentes = contar_ventas(conn)
    if existentes > 0:
        print(f"[initial_load] Ya hay {existentes} filas en raw.ventas. Se omite la ingesta inicial.")
        conn.close()
        return

    print(f"[initial_load] Insertando {INITIAL_ROWS} filas iniciales...")
    ventas = [generar_venta(historico=True) for _ in range(INITIAL_ROWS)]
    insertar_ventas(conn, ventas)
    print(f"[initial_load] Ingesta inicial completada. Total: {contar_ventas(conn)} filas.")
    conn.close()


if __name__ == "__main__":
    main()
