from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule
from prefect.flow_runners import SubprocessFlowRunner

DeploymentSpec(
    name="cron-schedule-deployment",
    flow_location="./homework.py",
    flow_runner=SubprocessFlowRunner(),
    schedule=CronSchedule(
        cron="0 9 15 * *",  # https://bradymholt.github.io/cron-expression-descriptor/
        timezone="America/New_York",
    ),
    tags=["test_deploy"],
)

# poetry run prefect storage ls
# poetry run prefect storage create
# poetry run prefect deployment create homework.py
# poetry run prefect work-queue preview 08cafa27-88fb-4bf6-9891-d0f790ace046 --hours 4000


# ┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Scheduled Start Ti… ┃ Run ID                         ┃ Name         ┃ Deployment ID                 ┃
# ┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
# │ 2022-09-15 13:00:0… │ fd36324c-ace7-449e-83e1-57dff… │ white-iguana │ 0fb8a1a2-039d-454c-b62c-aa5a… │
# │ 2022-08-15 13:00:0… │ 5b7a8a07-2ef2-41a5-b7ee-a3ccf… │ orthodox-gr… │ 0fb8a1a2-039d-454c-b62c-aa5a… │
# │ 2022-07-15 13:00:0… │ 8032f6a4-ac6c-4ea2-8d21-09804… │ simple-liza… │ 0fb8a1a2-039d-454c-b62c-aa5a… │
# │ 2022-06-15 13:00:0… │ dd18c332-aab0-410e-a62f-8cbbc… │ careful-wax… │ 0fb8a1a2-039d-454c-b62c-aa5a… │
# └─────────────────────┴────────────────────────────────┴──────────────┴───────────────────────────────┘
#                                       (**) denotes a late run   # poetry run prefect work-queue ls


# poetry run prefect work-queue ls
#
#                              Work Queues
# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
# ┃                                   ID ┃ Name   ┃ Concurrency Limit ┃
# ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
# │ 08cafa27-88fb-4bf6-9891-d0f790ace046 │ global │ None              │
# └──────────────────────────────────────┴────────┴───────────────────┘
