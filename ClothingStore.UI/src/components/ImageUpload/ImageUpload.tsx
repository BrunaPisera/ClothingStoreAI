import { useMemo, type ChangeEvent } from 'react';

interface ImageUploadProps {
  file: File | null;
  onFileChange: (file: File | null) => void;
}

function ImageUpload({ file, onFileChange }: ImageUploadProps) {
  const previewUrl = useMemo(() => {
    if (!file) return null;
    return URL.createObjectURL(file);
  }, [file]);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const chosenFile = event.target.files?.[0] ?? null;
    onFileChange(chosenFile);
  };

  return (
    <div className="image-upload-card">
      <label className="image-upload-label" htmlFor="productImage">
        <div className="upload-dropzone">
          {previewUrl ? (
            <img src={previewUrl} alt="Product preview" className="preview-image" />
          ) : (
            <div className="upload-prompt">
              <strong>Select an image</strong>
              <span>Upload a single clothing item photo for visual analysis</span>
            </div>
          )}
        </div>
      </label>

      <input
        id="productImage"
        type="file"
        accept="image/*"
        multiple={false}
        onChange={handleFileChange}
        hidden
      />

      <p className="hint-text">
        Only one image per submission. Send a photo of one clothing piece only.
      </p>
    </div>
  );
}

export default ImageUpload;
