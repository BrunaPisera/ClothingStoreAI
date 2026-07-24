using ClothingStoreAI.Application.Configuration;
using ClothingStoreAI.Application.Interfaces;
using ClothingStoreAI.Infrastructure.Prompts;
using Microsoft.Extensions.Options;
using OpenAI;
using OpenAI.Chat;

namespace ClothingStoreAI.Infrastructure.Services
{
    public class ImageAnalysisService : IImageAnalysisService
    {
        private readonly OpenAiOptions _options;
        private readonly OpenAIClient _client;
        private readonly IImageProcessor _imageProcessor;
        private readonly ChatClient _chatClient;

        public ImageAnalysisService(IOptions<OpenAiOptions> options, IImageProcessor imageProcessor)
        {
            _options = options.Value;
            _client = new OpenAIClient(_options.ApiKey);
            _chatClient = _client.GetChatClient(_options.Model);

            _imageProcessor = imageProcessor;
        }

        public async Task<string> AnalyzeImageAsync(byte[] image)
        {
            var resizedImage =
                await _imageProcessor.ResizeIfNeededAsync(image);
           
            var messages = CreateMessages(resizedImage);
            Console.WriteLine(messages);
            return await GetResponseAsync(messages);
        }

        private static List<ChatMessage> CreateMessages(byte[] image)
        {
            return
            [
                new UserChatMessage(
                [
                    ChatMessageContentPart.CreateTextPart(ImageAnalysisPrompt.Prompt),
                    ChatMessageContentPart.CreateImagePart(
                        BinaryData.FromBytes(image),
                        "image/jpeg")
                ])
            ];
        }

        private async Task<string> GetResponseAsync(List<ChatMessage> messages)
        {            
            var completion =
                await _chatClient.CompleteChatAsync(messages);

            //Console.WriteLine();
            //Console.WriteLine("========== TEST DE NUMERO: " + _counter + " ==========");
            //Console.WriteLine("========== IMAGE ANALYSIS ==========");
            //Console.WriteLine($"Input Tokens : {completion.Value.Usage.InputTokenCount}");
            //Console.WriteLine($"Output Tokens: {completion.Value.Usage.OutputTokenCount}");
            //Console.WriteLine($"Total Tokens : {completion.Value.Usage.TotalTokenCount}");
            //Console.WriteLine("====================================");
            //Console.WriteLine();
            
            return completion.Value.Content[0].Text;
        }
    }
}
