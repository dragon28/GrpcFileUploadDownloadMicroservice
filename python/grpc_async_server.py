import asyncio
import grpc

import image_service_async_pb2
import image_service_async_pb2_grpc


filestorage_folder = "./filestorage/"

file_chunk_size = 1024

class ImageServiceServicer(image_service_async_pb2_grpc.ImageServiceServicer):
    
    async def StreamUploadImage(self, request_iterator, context):
        
        async for request in request_iterator:
            
            with open(filestorage_folder + request.name, 'ab') as fileab:
                
                fileab.write(request.image_chunk)
                
        return image_service_async_pb2.ImageUploadResponse(message="Image uploaded successfully")

    
    async def StreamDownloadImage(self, request, context):
        
        with open(filestorage_folder + request.name, 'rb') as filerb:
            
            while chunk := filerb.read(file_chunk_size):
                
                yield image_service_async_pb2.ImageDownloadResponse(image_chunk=chunk)


async def main():
    
    server = grpc.aio.server()
    
    image_service_async_pb2_grpc.add_ImageServiceServicer_to_server(ImageServiceServicer(), server)
    
    listen_addr = '[::]:50051'
    
    server.add_insecure_port(listen_addr)
    
    await server.start()
    
    await server.wait_for_termination()


if __name__ == '__main__':
    
    asyncio.run(main())