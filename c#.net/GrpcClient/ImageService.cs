using System.IO;
using System.Threading.Tasks;
using Grpc.Net.Client;
using GrpcImageClient;

public class ImageClient
{
    private readonly ImageService.ImageServiceClient _client;

    public ImageClient(ImageService.ImageServiceClient client)
    {
        _client = client;
    }

    public async Task UploadImageAsync(string imagePath)
    {
        using var call = _client.Upload();

        // Read the image data from a file
        var imageData = await File.ReadAllBytesAsync(imagePath);

        // Send the image data to the server
        await call.RequestStream.WriteAsync(new ImageFile { Name = imagePath, Data = Google.Protobuf.ByteString.CopyFrom(imageData) });

        await call.RequestStream.CompleteAsync();

        var response = await call.ResponseAsync;

        Console.WriteLine("Upload status: " + response.Status);
    }

    public async Task DownloadImageAsync(string imageName)
    {
        var responseStream = _client.Download(new ImageRequest { Name = imageName });

        while (await responseStream.ResponseStream.MoveNext(CancellationToken.None))
        {
            var imageData = responseStream.ResponseStream.Current;

            // Save the image data to a file
            await File.WriteAllBytesAsync(imageName, imageData.Data.ToByteArray());
        }
    }
}