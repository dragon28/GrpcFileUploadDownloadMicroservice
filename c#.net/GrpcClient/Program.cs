using System;
using System.Threading.Tasks;
using Grpc.Net.Client;
using GrpcImageClient;

class Program
{
    static async Task Main(string[] args)
    {
        // Create a channel
        using var channel = GrpcChannel.ForAddress("http://localhost:6886");

        // Create a service client
        var serviceClient = new ImageService.ImageServiceClient(channel);

        // Create an ImageClient
        var client = new ImageClient(serviceClient);

        // Call the UploadImageAsync method
        await client.UploadImageAsync("gold.jpg");

        // Call the DownloadImageAsync method
        //await client.DownloadImageAsync("gold.jpg");

        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }
}