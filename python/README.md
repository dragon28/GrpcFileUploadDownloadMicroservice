Please make sure that you have installed Python version 3.10

Requirements:

Install gRPC:

`python -m pip install grpcio`

or

`python3 -m pip install grpcio`


 Install gRPC tools:

 `python -m pip install grpcio-tools`

 or

 `python3 -m pip install grpcio-tools`



Generate Protobuf files:

image_service.proto:

`python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./image_service.proto`

or

`python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./image_service.proto`



image_service_async.proto:

`python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./image_service_async.proto`

or

`python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. ./image_service_async.proto`
