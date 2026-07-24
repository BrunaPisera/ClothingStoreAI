export interface ProductAnalysisResponse {
  message?: string | null;
  description?: string;
  suggestedPrice?: number;
}

export interface AnalyzeProductPayload {
  image: File;
  costPrice: number;
}
