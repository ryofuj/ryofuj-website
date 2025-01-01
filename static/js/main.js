document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('search-input');
  const tileElements = document.querySelectorAll('.tile');
  const modalOverlay = document.getElementById('modal-overlay');
  const modalContent = document.getElementById('modal-content');
  const modalClose = document.getElementById('modal-close');
  const filterCheckboxes = document.querySelectorAll('.filter-tags input[type="checkbox"]');

  function applyFilters() {
    const query = searchInput.value.toLowerCase();
    const selectedTags = Array.from(filterCheckboxes)
      .filter(chk => chk.checked)
      .map(chk => chk.value);

    tileElements.forEach(tile => {
      const text = tile.innerText.toLowerCase();
      const tileTags = tile.dataset.tags ? tile.dataset.tags.split(',') : [];
      const matchesSearch = text.includes(query);
      const matchesTags = selectedTags.every(tag => tileTags.includes(tag));

      if (matchesSearch && matchesTags) {
        tile.style.display = '';
      } else {
        tile.style.display = 'none';
      }
    });
  }

  searchInput.addEventListener('input', applyFilters);
  filterCheckboxes.forEach(chk => {
    chk.addEventListener('change', applyFilters);
  });

  tileElements.forEach(tile => {
    tile.addEventListener('click', () => {
      const title = tile.querySelector('h2') ? tile.querySelector('h2').innerText : '';
      const subtitle = tile.querySelector('.subtitle-holder') ? tile.querySelector('.subtitle-holder').innerText : '';
      const longDesc = tile.dataset.longdesc || '';
      const imageSrc = tile.dataset.image || '';
      const linkHref = tile.dataset.link || '';

      if (!title) return;

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
