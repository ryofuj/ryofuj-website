/* =========================================
   src/components/Carousel.jsx
   ========================================= */
   import React, { useEffect, useState } from 'react';

   /**
    * Carousel
    * @param {string[]} images - An array of image URLs
    * @param {number} interval - Milliseconds between auto-slide (default 3000)
    */
   function Carousel({ images = [], interval = 3000 }) {
     const [activeIndex, setActiveIndex] = useState(0);
   
     useEffect(() => {
       if (images.length === 0) return;
   
       // Auto-advance the carousel every 'interval' ms
       const timer = setInterval(() => {
         setActiveIndex((prevIndex) => (prevIndex + 1) % images.length);
       }, interval);
   
       return () => clearInterval(timer);
     }, [images.length, interval]);
   
     // Handle manual navigation
     const goToIndex = (index) => {
       setActiveIndex(index);
     };
   
     if (!images.length) {
       return <p>No images to display</p>;
     }
   
     return (
       <div style={{ position: 'relative', textAlign: 'center' }}>
         {/* Current Image */}
         <img
           src={images[activeIndex]}
           alt={`Slide ${activeIndex + 1}`}
           style={{ maxWidth: '100%', maxHeight: '400px', objectFit: 'cover', borderRadius: '8px' }}
         />
   
         {/* Navigation Dots */}
         <div style={{ position: 'absolute', bottom: '10px', left: '50%', transform: 'translateX(-50%)' }}>
           {images.map((_, idx) => (
             <span
               key={idx}
               onClick={() => goToIndex(idx)}
               style={{
                 display: 'inline-block',
                 width: '12px',
                 height: '12px',
                 margin: '0 5px',
                 borderRadius: '50%',
                 backgroundColor: idx === activeIndex ? '#fff' : 'rgba(255, 255, 255, 0.5)',
                 cursor: 'pointer',
                 boxShadow: '0 0 2px rgba(0,0,0,0.5)'
               }}
             />
           ))}
         </div>
       </div>
     );
   }
   
   export default Carousel;
   