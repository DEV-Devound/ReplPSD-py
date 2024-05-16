// En src/App.js
import React, { useState } from 'react';
import InputField from './components/InputField';

export default function App() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:3000/write', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        first_name: formData.firstName,
        last_name: formData.lastName,
      }),
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="app-container">
      <form onSubmit={handleSubmit}>
        <InputField label="First name.." name="firstName" onChange={handleChange} />
        <InputField label="Last name.." name="lastName" onChange={handleChange} />
        <button type="submit">Generate</button>
      </form>
    </div>
  );
}