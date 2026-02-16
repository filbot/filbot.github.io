console.log("Custom JavaScript loaded");

// Image Lightbox
(function() {
  'use strict';

  // Create lightbox overlay element
  const overlay = document.createElement('div');
  overlay.className = 'lightbox-overlay';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-label', 'Image lightbox');
  overlay.setAttribute('aria-modal', 'true');
  
  const overlayImg = document.createElement('img');
  overlayImg.alt = '';
  overlay.appendChild(overlayImg);
  
  // Add overlay to body when DOM is ready
  function init() {
    document.body.appendChild(overlay);
    
    // Find all images in content/markdown areas
    const contentImages = document.querySelectorAll('.content img, .markdown-image img, article img, .responsive-image img, figure img');
    
    contentImages.forEach(img => {
      // Make images clickable
      img.style.cursor = 'pointer';
      img.setAttribute('tabindex', '0');
      img.setAttribute('role', 'button');
      img.setAttribute('aria-label', 'Click to view full size');
      
      // Click handler
      img.addEventListener('click', function(e) {
        e.preventDefault();
        openLightbox(this.src, this.alt);
      });
      
      // Keyboard support for images
      img.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openLightbox(this.src, this.alt);
        }
      });
    });
    
    // Close lightbox on click
    overlay.addEventListener('click', closeLightbox);
    
    // Close on ESC key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && overlay.classList.contains('active')) {
        closeLightbox();
      }
    });
  }
  
  function openLightbox(src, alt) {
    overlayImg.src = src;
    overlayImg.alt = alt || 'Full size image';
    document.body.classList.add('lightbox-active');
    overlay.classList.add('active');
    
    // Force reflow for animation
    overlay.offsetHeight;
  }
  
  function closeLightbox() {
    overlay.classList.remove('active');
    document.body.classList.remove('lightbox-active');
    // Clear image after transition
    setTimeout(() => {
      overlayImg.src = '';
    }, 300);
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();