/* =========================================
   src/components/Carousel.jsx
   ========================================= */
   import React, { useEffect, useState } from 'react';

   /**
    * Carousel
    * @param {string[]} images - An array of image URLs
    * @param {number} interval - Milliseconds between auto-slide
    */
   function Carousel({ images = [], interval = 3000 }) {
     const [activeIndex, setActiveIndex] = useState(0);
   
     useEffect(() => {
       // Auto-advance the carousel every 'interval' ms
       const timer = setInterval(() => {
         setActiveIndex((prev) => (prev + 1) % images.length);
       }, interval);
   
       return () => clearInterval(timer);
     }, [images, interval]);
   
     if (!images.length) {
       return <p>No images to display</p>;
     }
   
     // Ensure index is valid
     const currentIndex = activeIndex < images.length ? activeIndex : 0;
     const currentImage = images[currentIndex];
   
     return (
       <div style={{ textAlign: 'center' }}>
         {/* Display the current image */}
         <img
           src={currentImage}
           alt={`Carousel item ${currentIndex + 1}`}
           style={{ maxWidth: '100%', display: 'block', margin: '0 auto' }}
         />
   
         {/* Dots for manual nav (optional) */}
         <div style={{ marginTop: '1rem' }}>
           {images.map((_, idx) => (
             <span
               key={idx}
               onClick={() => setActiveIndex(idx)}
               style={{
                 cursor: 'pointer',
                 display: 'inline-block',
                 width: '10px',
                 height: '10px',
                 borderRadius: '50%',
                 margin: '0 5px',
                 backgroundColor: idx === currentIndex ? '#333' : '#ccc'
               }}
             />
           ))}
         </div>
       </div>
     );
   }
   
   export default Carousel;
   