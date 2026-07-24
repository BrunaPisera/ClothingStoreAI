namespace ClothingStoreAI.Application.DTOs
{
    public class PricePredictionRequest
    {
        public string Category { get; set; } = "";
        public string SleeveType { get; set; } = "";
        public string Premium { get; set; } = "";
        public decimal CostPrice { get; set; }
    }
}
