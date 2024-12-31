document.addEventListener('DOMContentLoaded', () => {
    const slideshows = document.querySelectorAll('.slideshow-container');
  
    slideshows.forEach((slideshow) => {
      const slides = slideshow.querySelectorAll('.slide');
      let currentSlide = 0;
  
      if (slides.length > 0) slides[0].style.left = '0'; // Show the first slide
  
      setInterval(() => {
        if (slides.length > 1) {
          slides[currentSlide].style.left = '-100%'; // Move current slide out
          currentSlide = (currentSlide + 1) % slides.length; // Next slide
          slides[currentSlide].style.left = '0'; // Bring new slide in
        }
      }, 4000); // Slide interval (4 seconds)
    });
  });
  