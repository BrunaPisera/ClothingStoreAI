namespace ClothingStoreAI.Application.DTOs
{
    public class AnalyzeProductRequest
    {
        public byte[] Image { get; set; } = [];

        public decimal CostPrice { get; set; }
    }
}
