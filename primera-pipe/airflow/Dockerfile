FROM docker:cli AS docker-cli

FROM apache/airflow:2.10.3-python3.12

# Cliente de Docker (sin daemon): permite que las tareas (BashOperator)
# hagan 'docker run' contra el socket montado en /var/run/docker.sock.
COPY --from=docker-cli /usr/local/bin/docker /usr/local/bin/docker

COPY entrypoint-scheduler.sh /entrypoint-scheduler.sh

USER root
RUN chmod +x /entrypoint-scheduler.sh
USER airflow
