import React, { useState } from 'react';
import Logo from './components/Logo';
import CategoryItem from './components/CategoryItem';
import TemplateItem from './components/TemplateItem';
import SearchBar from './components/SearchBar';
import InputField from './components/InputField';
import ResultImage from './components/ResultImage';
import FileUploadButton from './components/FileUploadButton'; // Importa el nuevo componente

export default function App() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    psdFile: null, // Nuevo estado para almacenar el archivo PSD
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleFileSelect = (e) => {
    setFormData(prevFormData => ({
      ...prevFormData,
      psdFile: e.target.files[0], // Actualiza el estado con el archivo seleccionado
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append('first_name', formData.firstName);
    data.append('last_name', formData.lastName);
    if (formData.psdFile) {
      data.append('psd_file', formData.psdFile);
    }

    fetch('http://localhost:3002/write', {
      method: 'POST',
      body: data, // No necesitas especificar el Content-Type en este caso
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="app-container">
      <div style={{width: '10%', height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <Logo />
        <CategoryItem icon="fas fa-file-alt" text="TX" />
        <CategoryItem icon="fas fa-file-alt" text="WA" />
        <CategoryItem icon="fas fa-file-alt" text="AR" />
      </div>
      <div style={{width: '25%', padding: '0 1rem'}}>
        <SearchBar />
        <div style={{marginTop: '1rem'}}>
          <TemplateItem flag="fas fa-flag-usa" name="Texas" />
          <TemplateItem flag="fas fa-flag-usa" name="Washington" />
          <TemplateItem flag="fas fa-flag-usa" name="Arkansas" />
        </div>
      </div>
      <div style={{width: '20%', padding: '0 1rem'}}>
        <form onSubmit={handleSubmit}>
          <div style={{marginBottom: '1rem'}}>
            <InputField label="First name.." name="firstName" onChange={handleChange} />
            <InputField label="Last name.." name="lastName" onChange={handleChange} />
            <FileUploadButton onFileSelect={handleFileSelect} />
          </div>
          <button type="submit">Generate</button>
        </form>
      </div>
      <div style={{width: '45%', padding: '0 1rem'}}>
        <h2 style={{fontSize: '1.25rem', marginBottom: '1rem'}}>Texas Template 2021</h2>
        <ResultImage description="PLACEHOLDER IMAGE" />
        <h6 style={{fontSize: '0.85rem', marginBottom: '0.5rem'}}>FRONT SIDE</h6>
        <ResultImage description="PLACEHOLDER IMAGE 2" />
      </div>
    </div>
  );
}