// static/js/typewriter.js

document.addEventListener('DOMContentLoaded', () => {
    const introText = document.getElementById('typewriter-intro').textContent;
    const introElement = document.getElementById('typewriter-intro');
    introElement.textContent = '';  // Clear existing text

    let index = 0;
    const speed = 100;  // Typing speed in milliseconds

    function typeWriter() {
        if (index < introText.length) {
            introElement.textContent += introText.charAt(index);
            index++;
            setTimeout(typeWriter, speed);
        }
    }

    typeWriter();
});
