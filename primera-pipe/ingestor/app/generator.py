import random
import uuid
from datetime import datetime, timedelta, timezone

from faker import Faker

fake = Faker("es_ES")

CATALOGO = {
    "Portatil":    ("Informatica", (400, 2000)),
    "Raton":       ("Informatica", (10, 80)),
    "Teclado":     ("Informatica", (20, 150)),
    "Monitor":     ("Informatica", (100, 700)),
    "Auriculares": ("Audio", (15, 300)),
    "Altavoz":     ("Audio", (25, 400)),
    "Camara":      ("Fotografia", (200, 1500)),
    "Objetivo":    ("Fotografia", (100, 1200)),
    "Silla":       ("Mobiliario", (50, 500)),
    "Mesa":        ("Mobiliario", (60, 600)),
}


def generar_venta(historico=False):
    producto = random.choice(list(CATALOGO.keys()))
    categoria, (p_min, p_max) = CATALOGO[producto]
    cantidad = random.randint(1, 5)
    precio_unit = round(random.uniform(p_min, p_max), 2)
    total = round(precio_unit * cantidad, 2)

    if historico:
        # Ingesta inicial: repartida en los ultimos 30 dias
        segundos = random.randint(0, 60 * 60 * 24 * 30)
        creado_en = datetime.now(timezone.utc) - timedelta(seconds=segundos)
    else:
        # Ingesta continuada: evento "ahora"
        creado_en = datetime.now(timezone.utc)

    return {
        "uuid": str(uuid.uuid4()),
        "cliente": fake.name(),
        "email": fake.email(),
        "producto": producto,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio_unit": precio_unit,
        "total": total,
        "pais": fake.country(),
        "creado_en": creado_en,
    }
