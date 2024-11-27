import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/kshitijs22/basic-mlops.mlflow')
dagshub.init(repo_owner='kshitijs22', repo_name='basic-mlops', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)