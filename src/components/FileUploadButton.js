// En src/components/FileUploadButton.js
import React from 'react';

export default function FileUploadButton({ onFileSelect }) {
  return (
    <div>
      <input type="file" accept=".psd" onChange={onFileSelect} style={{ display: 'none' }} id="file" />
      <label htmlFor="file" style={{ cursor: 'pointer', padding: '10px', border: '1px solid #ccc', borderRadius: '5px', display: 'inline-block' }}>
        Upload PSD
      </label>
    </div>
  );
}