import React from 'react';

export default function CategoryItem({ icon, text }) {
  return (
    <div className="flex-container">
      <i className={`${icon} text-2xl`}></i>
      <span className="text-xs mt-2">{text}</span>
    </div>
  );
}