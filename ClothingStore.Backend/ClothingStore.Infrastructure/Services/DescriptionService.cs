using ClothingStoreAI.Application.Configuration;
using ClothingStoreAI.Application.Interfaces;
using ClothingStoreAI.Infrastructure.Prompts;
using Microsoft.Extensions.Options;
using OpenAI;
using OpenAI.Chat;

namespace ClothingStoreAI.Infrastructure.Services
{
    public class DescriptionService : IDescriptionService
    {
        private readonly OpenAiOptions _options;
        private readonly OpenAIClient _client;

        public DescriptionService(IOptions<OpenAiOptions> options)
        {
            _options = options.Value;
            _client = new OpenAIClient(_options.ApiKey);
        }

        public async Task<string> GenerateAsync(string attributes)
        {
            ChatClient chatClient = _client.GetChatClient(_options.Model);

            var messages = new List<ChatMessage>
            {
                new SystemChatMessage(DescriptionPromptPtBr.Prompt),
                new UserChatMessage(attributes)
            };

            ChatCompletion completion = await chatClient.CompleteChatAsync(messages);
            var description = completion.Content[0].Text;

            return description.Trim();
        }
    }
}
