from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize the DAG
dag = DAG(
    'mlops_pipeline',
    default_args=default_args,
    description='An example MLOps pipeline',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    tags=['mlops'],
)

def extract_data():
    # Placeholder for data extraction logic
    print("Extracting data...")

def preprocess_data():
    # Placeholder for data preprocessing logic
    print("Preprocessing data...")

def train_model():
    # Placeholder for model training logic
    print("Training model...")

def deploy_model():
    # Placeholder for model deployment logic
    print("Deploying model...")

# Define tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

deploy_task = PythonOperator(
    task_id='deploy_model',
    python_callable=deploy_model,
    dag=dag,
)

# Set task dependencies
extract_task >> preprocess_task >> train_task >> deploy_task
