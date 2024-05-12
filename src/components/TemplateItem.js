import React from 'react';

export default function TemplateItem({ flag, name }) {
  return (
    <div className="flex-box">
      <i className={`${flag} text-lg`}></i>
      <span className="ml-2">{name}</span>
    </div>
  );
}