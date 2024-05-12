import React from 'react';

export default function ResultImage({ description }) {
  return (
    <img src={`https://placehold.co/600x300?text=${description}`} alt={description} />
  );
}