using ClothingStoreAI.Application.DTOs;

namespace ClothingStoreAI.Application.Interfaces
{
    public interface IProductAnalysisService
    {
        Task<AnalyzeProductResponse> AnalyzeAsync(AnalyzeProductRequest request);
    }
}
