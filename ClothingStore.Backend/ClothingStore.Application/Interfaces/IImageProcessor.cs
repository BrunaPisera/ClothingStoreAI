using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClothingStoreAI.Application.Interfaces
{
    public interface IImageProcessor
    {
        Task<byte[]> ResizeIfNeededAsync(byte[] image);
    }
}
