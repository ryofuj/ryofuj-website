/* =========================================
   src/components/ProjectTile.jsx
   ========================================= */
   import React from 'react';
   import LazyLoad from 'react-lazyload';
   
   function ProjectTile({ project, onClick }) {
     return (
       <div
         id={`tile-${project.id}`}
         onClick={onClick}
         className="w-72 border rounded-lg cursor-pointer text-center p-4 shadow-md transition-transform transform hover:scale-105 hover:shadow-lg bg-white"
       >
         <LazyLoad height={200} offset={100} once>
           {project.image_url ? (
             <img
               src={project.image_url}
               alt={`${project.title} - ${project.company}`}
               className="w-full h-48 object-contain mb-4"
             />
           ) : (
             <div className="h-48 bg-gray-200 mb-4 flex items-center justify-center">
               <span className="text-gray-500">No Image</span>
             </div>
           )}
         </LazyLoad>
         <h3 className="text-xl font-semibold mb-2">{project.title}</h3>
         <p className="text-gray-600">{project.company}</p>
       </div>
     );
   }
   
   export default ProjectTile;
   