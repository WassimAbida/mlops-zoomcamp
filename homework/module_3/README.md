## Using prefect for ML experiments orchestration 

 - Create a VM on Cloud Provider of Choice

 - Open port 4200 ingress on the VM from 0.0.0.0/0 (all traffic) as well as HTTP in.
```
   pip install prefect 2.0
```

 - Set the UI_API_URL with :
```
prefect config set PREFECT_ORION_UI_API_URL="http://<external-ip>:4200/api"
```

- Start Orion with:
``` 
prefect orion start --host 0.0.0.0
```


 - From local machine, configure to hit the API with:
```
prefect config set PREFECT_API_URL="http://<external-ip>:4200/api"
```

 - The remote UI will be visible on :4200/