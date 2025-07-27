import subprocess

from prefect import flow

from src.gcs_to_bq import gcs_to_bq
from src.web_to_gcs import web_to_gcs


@flow
def run_dbt():
    """Run dbt transformations"""
    subprocess.run(["dbt", "run"], check=True)


@flow
def full_etl_pipeline():
    """Complete ETL: Web → GCS → BQ → dbt"""
    web_to_gcs()
    gcs_to_bq()
    run_dbt()


if __name__ == "__main__":
    full_etl_pipeline()
