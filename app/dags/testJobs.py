import airflow
from airflow import DAG
from airflow.contrib.operators.databricks_operator import DatabricksRunNowOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import timedelta, datetime

# default arguments
args = {
    'owner': 'Daniel',
    'depends_on_past': False,
    'databricks_conn_id':'my_databricks_conn'
}


with DAG(dag_id='testJobs', default_args=args, start_date=airflow.utils.dates.days_ago(1)) as dag:

    first_task = DummyOperator(
        task_id = 'first_task')
        
    notebook_1_task = DatabricksRunNowOperator(
        task_id='notebook_1',
        job_id=1,
        json= {
            "notebook_params": {
                "param1": "AnyParam"
            }},
        do_xcom_push=True
            )
    
    first_task >> notebook_1_task

