from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

DOCKER_NETWORK = "datanet"
# Copia sin comentarios del .env que usan ingestor/dbt (generada por el
# entrypoint del scheduler); evita pasar POSTGRES_* en texto plano por el
# comando y evita que 'docker run --env-file' tropiece con comentarios.
ENV_FILE = "/opt/airflow/project.clean.env"

default_args = {
    "owner": "data-eng",
    "retries": 1,
}


def docker_run(image: str, command: str) -> str:
    return (
        f"docker run --rm --network {DOCKER_NETWORK} --env-file {ENV_FILE} {image} {command}"
    )


with DAG(
    dag_id="pipeline_ventas",
    description="Ingesta batch + transformaciones dbt (raw -> staging -> test -> marts)",
    schedule="@hourly",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["ventas", "ingestor", "dbt"],
) as dag:

    batch_load = BashOperator(
        task_id="batch_load",
        bash_command=docker_run("ingesta-ingestor", "python -m app.batch_load"),
    )

    raw_to_staging = BashOperator(
        task_id="dbt_raw_to_staging",
        bash_command=docker_run("ingesta-dbt", "dbt run --select staging"),
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=docker_run("ingesta-dbt", "dbt test"),
    )

    staging_to_marts = BashOperator(
        task_id="dbt_staging_to_marts",
        bash_command=docker_run("ingesta-dbt", "dbt run --select marts"),
    )

    batch_load >> raw_to_staging >> dbt_test >> staging_to_marts
