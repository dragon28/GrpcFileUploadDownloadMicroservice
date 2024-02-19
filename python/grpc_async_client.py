import asyncio
import grpc

import image_service_async_pb2
import image_service_async_pb2_grpc

file_chunk_size = 1024

async def stream_upload_image(stub, image_path, image_name):
        
    request_iterator = generate_request_iterator(image_path, image_name)
    
    response = await stub.StreamUploadImage(request_iterator)
    
    print(response.message)


async def generate_request_iterator(image_path, image_name):
    
    with open(image_path, 'rb') as filerb:
        
        while chunk := filerb.read(file_chunk_size):
            
            yield image_service_async_pb2.ImageUploadRequest(image_chunk=chunk, name=image_name)


async def stream_download_image(stub, image_name):
        
    response_iterator = stub.StreamDownloadImage(image_service_async_pb2.ImageDownloadRequest(name=image_name))
    
    async for response in response_iterator:
        
        with open(image_name, 'ab') as fileab:
            
            fileab.write(response.image_chunk)


async def main():
    
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        
        stub = image_service_async_pb2_grpc.ImageServiceStub(channel)
        
        await stream_upload_image(stub, './gold.jpg', 'gold2.jpg')
        
        await stream_download_image(stub, 'gold2.jpg')


if __name__ == '__main__':
    
    asyncio.run(main())