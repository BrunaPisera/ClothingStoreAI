using System.Net.Http.Json;
using ClothingStoreAI.Application.DTOs;
using ClothingStoreAI.Application.Interfaces;

namespace ClothingStoreAI.Infrastructure.Services;

public class PriceSuggestionService : IPriceSuggestionService
{
    private readonly HttpClient _httpClient;

    public PriceSuggestionService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<decimal> SuggestPriceAsync(
        PricePredictionRequest request)
    {
        using var response = await _httpClient.PostAsJsonAsync(
            "predict",
            request);

        response.EnsureSuccessStatusCode();

        var prediction = await response.Content
            .ReadFromJsonAsync<PricePredictionResponse>();

        if (prediction is null)
        {
            throw new InvalidOperationException(
                "The price service returned an invalid response.");
        }

        return prediction.PredictedPrice;
    }
}