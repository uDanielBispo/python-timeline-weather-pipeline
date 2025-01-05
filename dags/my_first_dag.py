from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
import pendulum

with DAG(
    dag_id='my_first_dag',
    start_date=pendulum.today('UTC').add(days=-2), 
    schedule_interval='@daily'
) as dag:
    task_1 = EmptyOperator(task_id='task_1')
    task_2 = EmptyOperator(task_id='task_2')
    task_3 = EmptyOperator(task_id='task_3')

    task_4_bash = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir -p "/home/daniel/Documents/Alura/python_apache_airflow_pipeline/pasta={{data_interval_end}}"'
    )

    task_1 >> [task_2, task_3] 
    task_3 >> task_4_bash