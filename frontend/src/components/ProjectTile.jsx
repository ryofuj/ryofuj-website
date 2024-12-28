import React from 'react';

function ProjectTile({ project, onClick }) {
  return (
    <div
      id={`tile-${project.id}`}
      onClick={onClick}
      style={{
        width: '200px',
        border: '1px solid #ccc',
        cursor: 'pointer',
        textAlign: 'center',
        padding: '1rem',
        position: 'relative'
      }}
    >
      {project.image_url ? (
        <img
          src={project.image_url}
          alt={project.title}
          style={{ maxWidth: '100%', maxHeight: '150px' }}
        />
      ) : (
        <div style={{ height: '150px', background: '#eee' }}>
          No Image
        </div>
      )}
      <h4 style={{ marginTop: '0.5rem' }}>{project.title}</h4>
    </div>
  );
}

export default ProjectTile;
