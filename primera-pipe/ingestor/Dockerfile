FROM python:3.12-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir --retries 10 --timeout 120 -r requirements.txt

COPY app/ ./app/

# Comando por defecto al arrancar: la ingesta inicial (se ejecuta una vez y termina).
# El job de lotes se invoca bajo demanda (y en el futuro, desde Airflow).
CMD ["python", "-m", "app.initial_load"]
