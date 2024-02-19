using System.IO;
using System.Threading.Tasks;
using Grpc.Core;
//using Google.Protobuf;
using GrpcImageServer;

namespace GrpcImageServer.Services;

public class  ImagerService : ImageService.ImageServiceBase
{
    string filestorage = @"./filestorage/";

    public override async Task<ImageResponse> Upload(IAsyncStreamReader<ImageFile> requestStream, ServerCallContext context)
    {
        await foreach (var imageFile in requestStream.ReadAllAsync())
        {
            // Save the image data to a file
            await File.WriteAllBytesAsync(filestorage + imageFile.Name, imageFile.Data.ToByteArray());
        }

        return new ImageResponse { Status = "Upload successful" };
    }

    public override async Task Download(ImageRequest request, IServerStreamWriter<ImageData> responseStream, ServerCallContext context)
    {
        // Read the image data from a file
        var imageData = await File.ReadAllBytesAsync(filestorage + request.Name);

        // Send the image data to the client
        await responseStream.WriteAsync(new ImageData { Data = Google.Protobuf.ByteString.CopyFrom(imageData) });
    }
}
