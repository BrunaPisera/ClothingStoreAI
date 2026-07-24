import axios from 'axios';
import { ProductAnalysisResponse } from '../types/product';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:5000',
  headers: {
    Accept: 'application/json'
  }
});

export async function analyzeProduct(
  image: File,
  costPrice: number
): Promise<ProductAnalysisResponse> {

  const formData = new FormData();

  formData.append('image', image);
  formData.append('costPrice', costPrice.toString());

  const response = await api.post<ProductAnalysisResponse>(
    '/api/products/analyze',
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
  );

  return response.data;
}

export async function analyzeImage(
  image: File
): Promise<ProductAnalysisResponse> {

  const formData = new FormData();

  formData.append('image', image);

  const response = await api.post<ProductAnalysisResponse>(
    '/api/products/analyze-image',
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
  );

  return response.data;
}

export default api;