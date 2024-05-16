// En src/components/InputField.js
import React from 'react';
export default function InputField({ label, name, onChange }) {
  return (
    <input
      type="text"
      placeholder={label}
      name={name}
      onChange={onChange}
    />
  );
}