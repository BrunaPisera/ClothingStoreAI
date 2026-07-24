using ClothingStoreAI.Application.DTOs;
using ClothingStoreAI.Application.Interfaces;
using Microsoft.AspNetCore.Mvc;

namespace ClothingStoreAI.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ProductsController : ControllerBase
    {
        private readonly IProductAnalysisService _productAnalysisService;

        public ProductsController(IProductAnalysisService productAnalysisService)
        {
            _productAnalysisService = productAnalysisService;
        }

        [HttpPost("analyze")]
        public async Task<IActionResult> Analyze(
                        IFormFile image,
                        [FromForm] decimal costPrice)
        {
            if (image == null || image.Length == 0)
            {
                return BadRequest("Image is required.");
            }

            var request = new AnalyzeProductRequest
            {
                Image = await ConvertToByteArrayAsync(image),
                CostPrice = costPrice
            };

            var response = await _productAnalysisService.AnalyzeAsync(request);

            return Ok(response);
        }

        private static async Task<byte[]> ConvertToByteArrayAsync(IFormFile file)
        {
            using var memoryStream = new MemoryStream();
            await file.CopyToAsync(memoryStream);

            return memoryStream.ToArray();
        }
    }
}