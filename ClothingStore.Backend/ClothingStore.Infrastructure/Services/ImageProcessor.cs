using ClothingStoreAI.Application.Interfaces;
using SkiaSharp;

namespace ClothingStoreAI.Infrastructure.Services;

public class ImageProcessor : IImageProcessor
{
    private const int MaxWidth = 768;
    private const int MaxHeight = 768;

    public Task<byte[]> ResizeIfNeededAsync(byte[] image)
    {
        using var input = new MemoryStream(image);
        using var bitmap = SKBitmap.Decode(input);

        if (bitmap.Width <= MaxWidth && bitmap.Height <= MaxHeight)
        {
            return Task.FromResult(ConvertToJpeg(bitmap));
        }

        float ratio = Math.Min(
            (float)MaxWidth / bitmap.Width,
            (float)MaxHeight / bitmap.Height);

        int newWidth = (int)(bitmap.Width * ratio);
        int newHeight = (int)(bitmap.Height * ratio);

        using var resizedBitmap = bitmap.Resize(
            new SKImageInfo(newWidth, newHeight),
            new SKSamplingOptions(SKFilterMode.Linear));

        return Task.FromResult(ConvertToJpeg(resizedBitmap));
    }

    private static byte[] ConvertToJpeg(SKBitmap bitmap)
    {
        using var output = new MemoryStream();

        using var skImage = SKImage.FromBitmap(bitmap);

        using var data = skImage.Encode(
            SKEncodedImageFormat.Jpeg,
            80);

        data.SaveTo(output);

        return output.ToArray();
    }
}