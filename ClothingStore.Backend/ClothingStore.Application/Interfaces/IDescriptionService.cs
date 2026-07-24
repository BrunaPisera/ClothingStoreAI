using ClothingStoreAI.Application.DTOs;

namespace ClothingStoreAI.Application.Interfaces
{
    public interface IDescriptionService
    {
        Task<string> GenerateAsync(
            string attributes);

    }
}
