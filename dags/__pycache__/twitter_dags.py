import sys
sys.path.append("/home/daniel/Documents/airflow_dados_twiter")
from pathlib import Path


from airflow.models import DAG
from operators.twitter_operator import TwitterOperator
from os.path import join   
from airflow.utils.dates import days_ago
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
        dag_id = "Twitter",
        start_date=days_ago(2),
        schedule='@daily'
        ) as dag:
    BASE_FOLDER = join(
        str(Path("~/Documents").expanduser()),
        "airflow_dados_twiter/datalake/{stage}/twitter_datascience/{partition}",
)
    PARTITION_FOLDER_EXTRACT = "extract_date={{ data_interval_start.strftime('%Y-%m-%d') }}"

    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
    query = "datascience"

    twitter_operator = TwitterOperator(file_path=join(BASE_FOLDER.format(stage="Bronze", partition=PARTITION_FOLDER_EXTRACT),
                                        "datascience_{{ ds_nodash }}.json"),
                                        query=query,
                                        start_time="{{ data_interval_start.strftime('%Y-%m-%dT%H:%M:%S.00Z') }}",
                                        end_time="{{ data_interval_end.strftime('%Y-%m-%dT%H:%M:%S.00Z') }}",
                                        task_id="twitter_datascience")

    
    twitter_transform = SparkSubmitOperator(task_id="transform_twitter_datascience",
                                            application="/home/daniel/Documents/airflow_dados_twiter/src/spark/transformation.py",
                                            name="twitter_transformation",
                                            application_args=["--src", BASE_FOLDER.format(stage="Bronze", partition=PARTITION_FOLDER_EXTRACT),
                                            "--dest", BASE_FOLDER.format(stage="Silver", partition=""),
                                            "--process-date", "{{ ds }}"])
    
    twitter_insight = SparkSubmitOperator(task_id="insight_twitter_datascience",
                                        application="/home/daniel/Documents/airflow_dados_twiter/src/spark/insight_tweet.py",
                                        name="twitter_insight",
                                        application_args=["--src", BASE_FOLDER.format(stage="Silver", partition=""),
                                        "--dest", BASE_FOLDER.format(stage="Gold", partition=""),
                                        "--process-date", "{{ ds }}"])



    twitter_operator >> twitter_transform >> twitter_insight