import React, { useState } from 'react';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setResult(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('http://localhost:8000/upload/', {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();

      if (data.error) {
        setError(data.error);
      } else {
        setResult(data);
      }
    } catch (err) {
      setError('Server error. Make sure backend is running.');
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit} style={{ marginBottom: '1rem' }}>
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
          required
        />
        <button type="submit" style={{ marginLeft: '1rem' }}>
          Upload & Analyze
        </button>
      </form>

      {error && <p style={{ color: 'red' }}>❌ {error}</p>}

      {result && (
        <div>
          <h3>📊 Summary</h3>
          <p><strong>Rows:</strong> {result.summary.rows}</p>
          <p><strong>Columns:</strong> {result.summary.columns}</p>
          <p><strong>Target Column:</strong> {result.summary.target_column}</p>

          <h3>🤖 Model</h3>
          <p><strong>Algorithm:</strong> {result.model.algorithm}</p>
          <p><strong>Accuracy:</strong> {result.model.accuracy}</p>
        </div>
      )}
    </div>
  );
}

export default UploadForm;
