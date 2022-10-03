# Injestion App

This application will be a microservice that will be providing both on live and on demand the data needed to make the investments.

To run this application with the correct python path, set:
```
    export PYTHONPATH="${PYTHONPATH}:/home/nil/Documents/Projects/forecasting-app/injestion"
```


## gRPC
We will generate our gRPC connection inside of the proto folder.
Once we have this, we will run the following compiler:
```
    python -m grpc_tools.protoc \
        -I ./proto \
        --python_out ./proto \
        --grpc_python_out ./proto \
        ./proto/sp500.proto
```
Where we have the following parts:
- *-I ./proto*: where to look for the files that the proto buffer code imports
- *--python_out ./proto*: where to output the python files 
- *--grpc_python_out ./proto*: where to output the python files
- *./proto/status.proto*: file to the proto file that will be used to generate the python code.
Where we will look for the .proto files imports. inside of the proto folder.