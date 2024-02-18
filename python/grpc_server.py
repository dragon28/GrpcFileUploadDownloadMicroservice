import grpc
from concurrent import futures

import image_service_pb2
import image_service_pb2_grpc


filestorage_folder = "./filestorage/"


class ImageServiceServicer(image_service_pb2_grpc.ImageServiceServicer):
    
    
    def UploadImage(self, request, context):
        
        with open(filestorage_folder + request.name, 'wb') as filewb:
            
            filewb.write(request.image)
        
        return image_service_pb2.ImageUploadResponse(message="Image uploaded successfully")

    
    def DownloadImage(self, request, context):
        
        with open( filestorage_folder + request.name, 'rb') as filerb:
            
            image = filerb.read()
        
        return image_service_pb2.ImageDownloadResponse(image=image)


def main():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    image_service_pb2_grpc.add_ImageServiceServicer_to_server(ImageServiceServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    
    server.start()
    
    server.wait_for_termination()


if __name__ == '__main__':
    
    main()