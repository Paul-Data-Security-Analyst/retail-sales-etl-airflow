import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# Absolute path to ETL project (NO dynamic username)
PROJECT_PATH = "/home/ubuntu/etl_airflow_project"

if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

from pipeline import extract, transform, load, aggregate


with DAG(
    dag_id="retail_sales_etl",
    start_date=days_ago(1),
    schedule="@daily",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load
    )

    aggregate_task = PythonOperator(
        task_id="aggregate_task",
        python_callable=aggregate
    )

    extract_task >> transform_task >> load_task >> aggregate_task
