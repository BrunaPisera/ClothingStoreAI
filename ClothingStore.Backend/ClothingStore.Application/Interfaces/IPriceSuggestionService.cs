using ClothingStoreAI.Application.DTOs;

namespace ClothingStoreAI.Application.Interfaces
{
    public interface IPriceSuggestionService
    {
        Task<decimal> SuggestPriceAsync(
            PricePredictionRequest attributes);
    }
}
