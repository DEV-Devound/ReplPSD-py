import React from 'react';
import Logo from './components/Logo';
import CategoryItem from './components/CategoryItem';
import TemplateItem from './components/TemplateItem';
import SearchBar from './components/SearchBar';
import InputField from './components/InputField';
import ResultImage from './components/ResultImage';

export default function App() {
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
        <div style={{marginBottom: '1rem'}}>
          <InputField label="First name.." />
          <InputField label="Last name.." />
        </div>
        <button>Generate</button>
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