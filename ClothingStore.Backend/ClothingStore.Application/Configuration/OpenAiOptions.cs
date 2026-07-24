namespace ClothingStoreAI.Application.Configuration
{
    public class OpenAiOptions
    {
        public const string SectionName = "OpenAI";

        public string ApiKey { get; set; } = string.Empty;

        public string Model { get; set; } = "gpt-4.1";
    }
}
