import React from 'react';

function Modal({ project, onClose }) {
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
