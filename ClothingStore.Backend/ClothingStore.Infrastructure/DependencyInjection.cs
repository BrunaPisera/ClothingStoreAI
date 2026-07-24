using ClothingStoreAI.Application.Configuration;
using ClothingStoreAI.Application.Interfaces;
using ClothingStoreAI.Application.Services;
using ClothingStoreAI.Infrastructure.Services;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace ClothingStoreAI.Infrastructure
{
    public static class DependencyInjection
    {
        public static IServiceCollection AddDependencyInjection(this IServiceCollection services, IConfiguration configuration)
        {
            services.Configure<OpenAiOptions>(
                configuration.GetSection(OpenAiOptions.SectionName));

            services.AddScoped<IProductAnalysisService, ProductAnalysisService>();
            services.AddScoped<IImageProcessor, ImageProcessor>();
            services.AddScoped<IImageAnalysisService, ImageAnalysisService>();
            services.AddScoped<IProductAnalysisService, ProductAnalysisService>();
            //services.AddHttpClient<IPriceSuggestionService, PriceSuggestionService>(client =>
            //{
            //    client.BaseAddress = new Uri("http://localhost:8000/");
            //});
            var predictorUrl = configuration["PRICE_PREDICTOR_URL"]
                ?? throw new InvalidOperationException(
                    "PRICE_PREDICTOR_URL is not configured.");

            services.AddHttpClient<IPriceSuggestionService, PriceSuggestionService>(
                client =>
                {
                    client.BaseAddress = new Uri(
                        $"{predictorUrl.TrimEnd('/')}/");
                });
            services.AddScoped<IDescriptionService, DescriptionService>();
            services.AddScoped<IImageProcessor, ImageProcessor>();

            return services;
        }
    }
}
