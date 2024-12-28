import React, { useState, useEffect } from 'react';
import ProjectTile from './components/ProjectTile';
import Modal from './components/Modal';

function App() {
  const [projects, setProjects] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);

  useEffect(() => {
    // Fetch projects from Flask API
    fetch('/api/projects')
      .then((res) => res.json())
      .then((data) => setProjects(data))
      .catch((err) => console.error(err));
  }, []);

  // Listen for hash changes to open a specific modal
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash; // e.g. "#project-2"
      if (hash.startsWith('#project-')) {
        const projectId = hash.replace('#project-', '');
        // Attempt to find the project in our local array
        const proj = projects.find((p) => p.id === Number(projectId));
        if (proj) {
          setSelectedProject(proj);
          // Optional: Smooth scroll to tile
          const tile = document.getElementById(`tile-${proj.id}`);
          if (tile) {
            tile.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        } else {
          // Project not found => handle error or fallback
          alert('Project Not Found');
          setSelectedProject(null);
        }
      } else {
        // If hash is empty or doesn't match the pattern, close modal
        setSelectedProject(null);
      }
    };

    window.addEventListener('hashchange', handleHashChange);
    // Run once on mount (in case user loads page with a hash)
    handleHashChange();

    return () => {
      window.removeEventListener('hashchange', handleHashChange);
    };
  }, [projects]);

  const closeModal = () => {
    setSelectedProject(null);
    // Clear the hash in the URL
    window.location.hash = '';
  };

  return (
    <div className="App" style={{ padding: '1rem' }}>
      <h1>My Portfolio</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem' }}>
        {projects.map((project) => (
          <ProjectTile
            key={project.id}
            project={project}
            onClick={() => {
              window.location.hash = `project-${project.id}`;
            }}
          />
        ))}
      </div>

      {selectedProject && (
        <Modal onClose={closeModal} project={selectedProject} />
      )}
    </div>
  );
}

export default App;
