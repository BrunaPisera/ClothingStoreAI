using ClothingStoreAI.Application.DTOs;
using ClothingStoreAI.Application.Interfaces;
using System.Text.Json;

namespace ClothingStoreAI.Application.Services;

public class ProductAnalysisService : IProductAnalysisService
{
    private readonly IImageAnalysisService _imageAnalysisService;
    private readonly IPriceSuggestionService _priceSuggestionService;
    private readonly IDescriptionService _descriptionService;

    public ProductAnalysisService(
        IImageAnalysisService imageAnalysisService,
        IPriceSuggestionService priceSuggestionService,
        IDescriptionService descriptionService)
    {
        _imageAnalysisService = imageAnalysisService;
        _priceSuggestionService = priceSuggestionService;
        _descriptionService = descriptionService;
    }

    public async Task<AnalyzeProductResponse> AnalyzeAsync(
        AnalyzeProductRequest request)
    {
        var attributesJson =
            await _imageAnalysisService.AnalyzeImageAsync(request.Image);

        var imageAnalysis = Parse(attributesJson);

        if (!string.IsNullOrWhiteSpace(imageAnalysis.Message))
        {
            return new AnalyzeProductResponse
            {
                Message = imageAnalysis.Message
            };
        }

        if (imageAnalysis.PricingAttributes == null)
        {
            throw new InvalidOperationException(
                "Image analysis did not return pricing attributes.");
        }

        imageAnalysis.PricingAttributes.CostPrice = request.CostPrice;

        var suggestedPrice =
            await _priceSuggestionService.SuggestPriceAsync(
                imageAnalysis.PricingAttributes);

        var description =
            await _descriptionService.GenerateAsync(attributesJson);

        return new AnalyzeProductResponse
        {
            Description = description,
            SuggestedPrice = suggestedPrice
        };
    }

    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNameCaseInsensitive = true
    };

    private static ImageAnalysisResult Parse(string json)
    {
        var result = JsonSerializer.Deserialize<ImageAnalysisResult>(
            json,
            JsonOptions);

        if (result == null)
        {
            throw new InvalidOperationException(
                "Invalid image analysis response.");
        }

        return result;
    }
}