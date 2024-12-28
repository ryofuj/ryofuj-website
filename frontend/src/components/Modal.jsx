/* =========================================
   src/components/Model.jsx
   ========================================= */
   import React, { Suspense } from 'react';
   import { Canvas } from '@react-three/fiber';
   import { OrbitControls, useGLTF, Html } from '@react-three/drei';
   
   /**
    * SingleModel
    * @param {string} modelUrl - The path/URL to the .gltf or .glb model file
    * This loads the model using the useGLTF hook from @react-three/drei.
    */
   function SingleModel({ modelUrl }) {
     const { scene } = useGLTF(modelUrl, true, true, (error) => {
       console.error(`Error loading GLTF model from ${modelUrl}:`, error);
     });
   
     return <primitive object={scene} />;
   }
   
   /**
    * Model
    * @param {string} modelPath - The path/URL to the model file
    * @param {number} width - Canvas width (default 600px)
    * @param {number} height - Canvas height (default 400px)
    * This component wraps our 3D model in a Three.js <Canvas>, adding lights, controls, etc.
    */
   function Model({ modelPath, width = 600, height = 400 }) {
     if (!modelPath) {
       return <p>No 3D model available.</p>;
     }
   
     return (
       <div style={{ width, height, margin: '0 auto' }}>
         <Canvas
           style={{ width: '100%', height: '100%' }}
           camera={{ position: [0, 1.5, 3], fov: 50 }}
         >
           <Suspense
             fallback={
               <Html
                 center
                 style={{
                   color: 'white',
                   background: 'rgba(0,0,0,0.5)',
                   padding: '1rem',
                   borderRadius: '8px'
                 }}
               >
                 Loading 3D model...
               </Html>
             }
           >
             <ambientLight intensity={0.4} />
             <directionalLight position={[5, 10, 5]} intensity={1.2} />
             <SingleModel modelUrl={modelPath} />
             <OrbitControls />
           </Suspense>
         </Canvas>
       </div>
     );
   }
   
   export default Model;
   