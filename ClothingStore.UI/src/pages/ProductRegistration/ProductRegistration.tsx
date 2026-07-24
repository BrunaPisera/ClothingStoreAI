import { useState } from 'react';
import { analyzeProduct } from '../../services/api';
import { ProductAnalysisResponse } from '../../types/product';
import ImageUpload from '../../components/ImageUpload/ImageUpload';
import ProductResultCard from '../../components/ProductResultCard/ProductResultCard';

const initialResult: ProductAnalysisResponse | null = null;

function ProductRegistration() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [costPrice, setCostPrice] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ProductAnalysisResponse | null>(initialResult);
  const [approvedProducts, setApprovedProducts] = useState<ProductAnalysisResponse[]>([]);
  const [message, setMessage] = useState('');

  const isSubmitDisabled = !selectedFile || !costPrice || loading;
  const isApproveDisabled = !result || Boolean(result.message);

  const clearForm = () => {
    setSelectedFile(null);
    setCostPrice('');
  };

  const handleAnalyze = async () => {
    if (!selectedFile || !costPrice) {
      return;
    }

    setLoading(true);
    setResult(null);
    setMessage('');

    try {
      const analysis = await analyzeProduct(
        selectedFile,
        parseFloat(costPrice)
      );

      setResult(analysis);
    } catch (error) {
      console.error(error);

      setMessage(
        'Failed to analyze the product. Please ensure the local API is running and the endpoint is available.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleApprove = () => {
    if (!result) {
      return;
    }

    setApprovedProducts((current) => [...current, result]);
    clearForm();
    setResult(null);
    setMessage('Product approved and added to the list.');
  };

  const handleCancel = () => {
    clearForm();
    setResult(null);
    setMessage('Registration canceled.');
  };

  return (
    <section className="page-shell">
      <div className="form-panel">
        <div className="panel-header">
          <h2>Product Registration</h2>
          <p>Upload a product image and let AI identify its visual attributes.</p>
        </div>

        <ImageUpload
          file={selectedFile}
          onFileChange={setSelectedFile}
        />

        <label className="input-label" htmlFor="costPrice">
          Cost Price
        </label>

        <input
          id="costPrice"
          type="number"
          inputMode="decimal"
          min="0"
          step="0.01"
          placeholder="0.00"
          value={costPrice}
          onChange={(event) => setCostPrice(event.target.value)}
          className="text-input"
        />

        <button
          className="primary-button"
          onClick={handleAnalyze}
          disabled={isSubmitDisabled}
        >
          {loading ? 'Analyzing...' : 'Analyze Product'}
        </button>

        {message && (
          <div className="toast-message">
            {message}
          </div>
        )}
      </div>

      <div className="result-panel">
        {loading && (
          <p className="status-text">
            Please wait while the AI analyzes the image...
          </p>
        )}

        {result ? (
          <ProductResultCard
            result={result}
            isApproveDisabled={isApproveDisabled}
            onApprove={handleApprove}
            onCancel={handleCancel}
          />
        ) : (
          <div className="result-empty">
            <p>The product summary will appear here after the analysis.</p>
          </div>
        )}
      </div>

      {approvedProducts.length > 0 && (
        <section className="approved-products">
          <h3>Approved Products</h3>
          <div className="approved-table-wrapper">
            <table className="approved-table">
              <thead>
                <tr>
                  <th>Description</th>
                  <th>Suggested Price</th>
                </tr>
              </thead>
              <tbody>
                {approvedProducts.map((product, index) => (
                  <tr key={`${product.description ?? 'product'}-${index}`}>
                    <td>
                      {product.description ?? 'No description'}
                    </td>
                    <td>
                      {product.suggestedPrice != null
                        ? `R$ ${product.suggestedPrice.toFixed(2)}`
                        : 'No suggested price'}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}
    </section>
  );
}

export default ProductRegistration;
