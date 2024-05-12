import React from 'react';

export default function SearchBar() {
  return (
    <div className="search-container">
      <i className="fas fa-search text-gray-400"></i>
      <input type="text" placeholder="Search" />
    </div>
  );
}