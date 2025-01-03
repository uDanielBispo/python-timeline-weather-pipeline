import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('KEY')

date_start = datetime.today()
date_end = date_start + timedelta(days=7)

date_start = date_start.strftime('%Y-%m-%d')
date_end = date_end.strftime('%Y-%m-%d')

city = 'Boston'

URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date_start}/{date_end}?unitGroup=metric&include=days&key={key}&contentType=csv'


data = pd.read_csv(URL)
print(data.head())

file_path = f'/home/daniel/Documents/Alura/python_apache_airflow_pipeline/semana={date_start}/'
os.mkdir(file_path)

data.to_csv(file_path + 'raw_data.csv')
data[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperature.csv')
data[['datetime', 'description', 'icon']].to_csv(file_path + 'conditions.csv')

