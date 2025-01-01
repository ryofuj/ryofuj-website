document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('search-input');
  const tileElements = document.querySelectorAll('.tile');
  const modalOverlay = document.getElementById('modal-overlay');
  const modalContent = document.getElementById('modal-content');
  const modalClose = document.getElementById('modal-close');

  searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase();
    tileElements.forEach(tile => {
      const text = tile.innerText.toLowerCase();
      tile.style.display = text.includes(query) ? '' : 'none';
    });
  });

  tileElements.forEach(tile => {
    tile.addEventListener('click', () => {
      const title = tile.querySelector('h2') ? tile.querySelector('h2').innerText : '';
      const subtitle = tile.querySelector('.subtitle-holder') ? tile.querySelector('.subtitle-holder').innerText : '';
      const longDesc = tile.dataset.longdesc || '';
      const imageSrc = tile.dataset.image || '';
      const linkHref = tile.dataset.link || '#';

      if (title) {
        modalContent.innerHTML = `
          <button class="modal-close" id="modal-close">×</button>
          <img src="${imageSrc}" alt="${title}" class="modal-image">
          <h2>${title}</h2>
          <p><em>${subtitle}</em></p>
          <p>${longDesc}</p>
          <p><a href="${linkHref}" target="_blank">Open Link</a></p>
        `;
        document.getElementById('modal-close').addEventListener('click', () => {
          modalOverlay.classList.remove('show');
        });
        modalOverlay.classList.add('show');
      }
    });
  });

  modalClose.addEventListener('click', () => {
    modalOverlay.classList.remove('show');
  });

  modalOverlay.addEventListener('click', (e) => {
    if(e.target === modalOverlay) {
      modalOverlay.classList.remove('show');
    }
  });
});
