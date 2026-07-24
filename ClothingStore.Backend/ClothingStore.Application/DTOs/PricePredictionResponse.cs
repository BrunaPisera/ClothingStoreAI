using System.Text.Json.Serialization;

namespace ClothingStoreAI.Application.DTOs
{
    public class PricePredictionResponse
    {
        [JsonPropertyName("predicted_price")]
        public decimal PredictedPrice { get; set; }
    }
}
