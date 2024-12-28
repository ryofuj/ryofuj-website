import React, { useEffect, useState } from 'react';

function Modal({ project, onClose }) {
  const [activeIndex, setActiveIndex] = useState(0);

  // If you have multiple images, they could be in an array. 
  // For now, we just show one image (project.image_url). 
  // Adjust this to handle multiple images or a carousel.

  useEffect(() => {
    // Example of auto-scrolling carousel (if multiple images exist)
    // Here we only have one image, so it’s not doing much.
    const intervalId = setInterval(() => {
      // If you had an array of images, you’d do something like:
      // setActiveIndex((prev) => (prev + 1) % imagesArray.length);
    }, 3000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div
      style={{
        position: 'fixed',
        top: 0, 
        left: 0, 
        width: '100%',
        height: '100%',
        backgroundColor: 'rgba(0,0,0,0.5)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 999
      }}
      onClick={onClose}
    >
      <div
        style={{
          background: '#fff',
          padding: '2rem',
          width: '80%',
          maxWidth: '600px',
          position: 'relative'
        }}
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          style={{ position: 'absolute', top: '1rem', right: '1rem' }}
        >
          Close
        </button>
        <h2>{project.title}</h2>
        <p>{project.description}</p>

        {project.image_url && (
          <img
            src={project.image_url}
            alt={project.title}
            style={{ maxWidth: '100%', marginTop: '1rem' }}
          />
        )}
      </div>
    </div>
  );
}

export default Modal;
