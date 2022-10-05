# Injestion Notebooks

We will be making injestion & cleaning of data resources.
We will be consuming different APIs as well as will be making web scraping.

To run the Dockerfile, we should run:
```
    docker build -t injestion_notebooks .
    docker images   # we can check it was created correctly

    docker run -ti injestion_notebooks:v1
```

The 0X will be different APIs we will access to.
The 1X will be tools to get data from multiple resources.


## Other Resources
- [Investors Portfolio](https://www.dataroma.com/m/managers.php)
- [Track What Mutual Funds are doing](https://www.moneycontrol.com/mutual-funds/best-funds/equity.html)


### TODO:
- Consume all the APIs and process the data
- Create Rest APIs and gRPC for the injest of data, and make the statistical analysis on the other service
- Automatize consumtion
    - Creation of instances on AWS
    - Based on load, creation of more instances with K8s & KEDA
- With KafKa create async messages  --> good on performance for algorithm? If not while loop on consuming not read data with gRPC. Backend Golang can consume it this way.
- With Celery create async tasks



