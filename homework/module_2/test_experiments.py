from mlflow.tracking import MlflowClient
from mlflow.entities import ViewType


MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

print(client.list_experiments())

# client.create_experiment(name="my-cool-experiment")

runs = client.search_runs(experiment_ids='1',
						filter_string="",
						run_view_type=ViewType.ACTIVE_ONLY,
						max_results=5,
						order_by=["metrics.training_mse ASC"])

print("xx", runs[0].data.metrics)
print(runs[0].data.metrics['training_mse'])
print(len(runs))


for run in [runs[0]]:
	print(f"run id: {run.info.run_id}, rmse {run.data.metrics['training_mse']:.4f}")


run_id ="cdbc327e990f4c67a99965bbc5f29974"
model_uri = f"runs:/{run_id}/model"
import mlflow
# mlflow.register_model(model_uri, name="nyc-taxi-module-3")


model_name = "nyc-taxi-module-2"
latest_version = client.get_latest_versions(name=model_name)
print(latest_version)

client.transition_model_version_stage(name=model_name, version=4, stage="production",
									  archive_existing_versions=False)

# update description
client.update_model_version(name=model_name,
							version=4,
							description="wanted to push it to V5 today")


client.download_artifacts(run_id=run_id, path='preprocessor',dst_path='.')

# test_model(name=model_name, stage='Production', X_test=X_test, y_test=y_test)
