import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from b7jxvidylrsfm4veady9aa_.tasks import Model_1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "b7JXVidYlRSFM4veaDY9aA_", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "MtFyfi68"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2026, 1, 11, tz = "UTC"), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    Model_1_op = Model_1()
