from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
import pendulum

with DAG(
    dag_id='atividade_aula_4',
    start_date=pendulum.today('UTC').add(days=-1), #começa um dia atras
    schedule_interval='@daily'
) as dag:

    def cumprimentos():
        print("Hello World! Welcome to airflow!")

    airflow_hello_world = PythonOperator(
        task_id='print_hello_world',
        python_callable= cumprimentos
    )

    airflow_hello_world