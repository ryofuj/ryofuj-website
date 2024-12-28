/* =========================================
   src/App.jsx
   ========================================= */
   import React, { useState, useEffect } from 'react';
   // Example imports of your own components
   import ProjectTile from './components/ProjectTile';
   import Modal from './components/Modal';
   
   function App() {
     // State for the list of projects
     const [projects, setProjects] = useState([]);
     // State for the currently selected project (for modal)
     const [selectedProject, setSelectedProject] = useState(null);
     // State to show a loading indicator while fetching
     const [loading, setLoading] = useState(true);
   
     // Fetch projects from the Flask API on initial load
     useEffect(() => {
       fetch('/api/projects')
         .then((res) => res.json())
         .then((data) => {
           setProjects(data);
           setLoading(false);
         })
         .catch((err) => {
           console.error(err);
           setLoading(false);
         });
     }, []);
   
     // Listen for hash changes to open a specific project modal by ID
     useEffect(() => {
       const handleHashChange = () => {
         const hash = window.location.hash; // e.g. "#project-2"
         if (hash.startsWith('#project-')) {
           const projectIdStr = hash.replace('#project-', '');
           // Convert to number and find the project
           const projectId = Number(projectIdStr);
           const proj = projects.find((p) => p.id === projectId);
   
           if (proj) {
             setSelectedProject(proj);
             // Optional: scroll to tile
             const tile = document.getElementById(`tile-${proj.id}`);
             if (tile) {
               tile.scrollIntoView({ behavior: 'smooth', block: 'start' });
             }
           } else {
             // If project ID not found, handle fallback
             alert('Project not found.');
             setSelectedProject(null);
             // Clear hash
             window.location.hash = '';
           }
         } else {
           // If hash is cleared or doesn't match "#project-...", close modal
           setSelectedProject(null);
         }
       };
   
       // Attach event listener on component mount
       window.addEventListener('hashchange', handleHashChange);
       // Check if there's a hash on initial render
       handleHashChange();
   
       // Cleanup on unmount
       return () => {
         window.removeEventListener('hashchange', handleHashChange);
       };
     }, [projects]);
   
     // Close the modal and clear the URL hash
     const closeModal = () => {
       setSelectedProject(null);
       window.location.hash = '';
     };
   
     // If data is still loading, show a simple loader
     if (loading) {
       return (
         <div style={{ textAlign: 'center', marginTop: '2rem' }}>
           Loading projects...
         </div>
       );
     }
   
     return (
       <div className="App" style={{ padding: '1rem', fontFamily: 'sans-serif' }}>
         <h1>My Portfolio</h1>
   
         {/* 
           Display a grid (or flex) of project tiles. 
           Clicking a tile sets the URL hash, which triggers the modal.
         */}
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
   
         {/* If a project is selected, render the Modal */}
         {selectedProject && (
           <Modal
             project={selectedProject}
             onClose={closeModal}
           />
         )}
       </div>
     );
   }
   
   export default App;
   