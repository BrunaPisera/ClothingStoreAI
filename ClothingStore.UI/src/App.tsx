import ProductRegistration from './pages/ProductRegistration/ProductRegistration';

function App() {
  return (
    <div className="app-shell">
      <header className="app-header">
        <div>
          <h1>AI-Assisted Product Registration</h1>
          <p className="subtitle">
            Upload a product image, enter the cost price, and let AI identify its
            visual attributes.
          </p>
        </div>
      </header>
      <main>
        <ProductRegistration />
      </main>
    </div>
  );
}

export default App;
