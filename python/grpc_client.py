import grpc

import image_service_pb2
import image_service_pb2_grpc


def upload_image(stub, image_path, image_name):
    
    with open(image_path, 'rb') as filerb:
        
        image = filerb.read()
        
    response = stub.UploadImage(image_service_pb2.ImageUploadRequest(image=image, name=image_name))
    
    print(response.message)


def download_image(stub, image_name):
    
    response = stub.DownloadImage(image_service_pb2.ImageDownloadRequest(name=image_name))
    
    with open(image_name, 'wb') as filewb:
        
        filewb.write(response.image)


def main():
    
    with grpc.insecure_channel('localhost:50051') as channel:
        
        stub = image_service_pb2_grpc.ImageServiceStub(channel)
        
        upload_image(stub, './gold.jpg', 'gold2.jpg')
        
        download_image(stub, 'gold2.jpg')

if __name__ == '__main__':
    
    main()