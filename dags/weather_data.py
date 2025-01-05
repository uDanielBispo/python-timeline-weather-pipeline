from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add

import pendulum
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('KEY')

with DAG(
    dag_id='weather_data',
    start_date=pendulum.datetime(2024, 12, 15, tz='UTC'), 
    schedule_interval='0 0 * * 1', # executa toda segunda (em cron expression)
) as dag:
    
    create_week_folder = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir -p "/home/daniel/Documents/Alura/python_apache_airflow_pipeline/week={{data_interval_end.strftime("%Y-%m-%d")}}"'
    )

    def extract_data(data_interval_end):

        date_start = data_interval_end
        date_end = ds_add(data_interval_end, 7)

        city = 'Boston'
        URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date_start}/{date_end}?unitGroup=metric&include=days&key={key}&contentType=csv'

        print(URL)

        data = pd.read_csv(URL)
        print(data.head())

        file_path = f'/home/daniel/Documents/Alura/python_apache_airflow_pipeline/week={data_interval_end}/'

        data.to_csv(file_path + 'raw_data.csv')
        data[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperature.csv')
        data[['datetime', 'description', 'icon']].to_csv(file_path + 'conditions.csv')

    extract_wather_data = PythonOperator(
        task_id = 'extrai_dados',
        python_callable=extract_data,op_kwargs={'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    create_week_folder >> extract_wather_data