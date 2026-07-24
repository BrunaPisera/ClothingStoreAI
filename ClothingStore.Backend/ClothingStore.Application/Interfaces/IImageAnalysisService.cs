using ClothingStoreAI.Application.DTOs;

public interface IImageAnalysisService
{
    Task<string> AnalyzeImageAsync(byte[] image);
}