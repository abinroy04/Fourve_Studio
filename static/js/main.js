/**
* Template Name: Visible
* Template URL: https://bootstrapmade.com/visible-bootstrap-agency-template/
* Updated: May 22 2025 with Bootstrap v5.3.6
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  document.addEventListener('DOMContentLoaded', function() {
  const preloader = document.querySelector('#preloader');
  const preloaderVideo = document.querySelector('#preloader-video');
  
  if (preloader && preloaderVideo) {
    // Ensure the video plays
    preloaderVideo.play().catch(err => {
      console.log("Video autoplay was prevented:", err);
    });
    
    // Wait for both DOM and resources (like images) to be fully loaded
    window.addEventListener('load', function() {
      // Add small delay to allow the video to be visible for a minimum time
      setTimeout(function() {
        preloader.classList.add('fade-out');
        
        // Remove the preloader after the transition completes
        setTimeout(function() {
          preloader.style.display = 'none';
        }, 600); // Match this to the transition time in CSS
      }, 1000); // Adjust delay as needed
    });
  }
  });

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });


  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

  /**
   * Portfolio functionality
   */
  function initPortfolio() {
    // Filter items when filter button clicked
    const filterItems = document.querySelectorAll('.portfolio-filters .filter-item');
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    
    if (filterItems && portfolioItems) {
      // Add click event to each filter item
      filterItems.forEach(item => {
        item.addEventListener('click', function() {
          // Remove active class from all items
          filterItems.forEach(filter => filter.classList.remove('active'));
          
          // Add active class to clicked item
          this.classList.add('active');
          
          // Get filter value
          const filterValue = this.getAttribute('data-filter');
          
          // Show/hide portfolio items based on filter
          portfolioItems.forEach(portfolioItem => {
            if (filterValue === 'all' || portfolioItem.classList.contains(filterValue)) {
              portfolioItem.style.display = 'block';
            } else {
              portfolioItem.style.display = 'none';
            }
          });
        });
      });

      // Handle YouTube thumbnail fallbacks and clicks
      document.querySelectorAll('.youtube-thumbnail').forEach(img => {
        // Handle thumbnail loading errors
        img.addEventListener('error', function() {
          const fallbackUrl = this.getAttribute('data-fallback');
          if (fallbackUrl && this.src !== fallbackUrl) {
            this.src = fallbackUrl;
          } else {
            // Final fallback to default image
            this.src = "/static/img/misc/misc-square-6.webp";
          }
        });

        // Handle thumbnail clicks
        img.addEventListener('click', function() {
          const videoUrl = this.getAttribute('data-video-url');
          if (videoUrl) {
            window.open(videoUrl, '_blank');
          }
        });
      });


      // Pause videos when clicking away (for iframe embeds)
      document.querySelectorAll('.filter-item').forEach(item => {
        item.addEventListener('click', function() {
          // Pause all YouTube videos when filtering
          document.querySelectorAll('.youtube-embed').forEach(iframe => {
            const src = iframe.src;
            iframe.src = src; // Resetting src stops the video
          });
        });
      });
      
      // Fix external links in overlays
      document.querySelectorAll('.external-link').forEach(link => {
        link.addEventListener('click', function(event) {
          // Prevent the click from bubbling to parent elements
          event.stopPropagation();
          
          // Open link in new tab
          window.open(this.href, '_blank');
        });
      });
      
      // Ensure overlays handle clicks properly
      document.querySelectorAll('.portfolio-overlay').forEach(overlay => {
        overlay.addEventListener('click', function(event) {
          // Stop propagation to prevent triggering other clicks
          event.stopPropagation();
        });
      });
    }

    // Initialize image stacks
    initImageStacks();
  }

  /**
   * Image Stack functionality
   */
  function initImageStacks() {
    const imageStacks = document.querySelectorAll('.portfolio-content.image-stack');
    
    imageStacks.forEach((stack, stackIndex) => {
      // Get the image stack data
      const stackDataElement = stack.querySelector('.stack-images-data');
      if (!stackDataElement) return;
      
      const stackData = JSON.parse(stackDataElement.textContent);
      const mainImage = stack.querySelector('.stack-main-image');
      const currentImageSpan = stack.querySelector('.current-image');
      const totalImagesSpan = stack.querySelector('.total-images');
      const prevBtn = stack.querySelector('.stack-prev');
      const nextBtn = stack.querySelector('.stack-next');
      const portfolioInfo = stack.querySelector('.portfolio-info');
      
      // Add preview button for lightbox functionality if not already present
      if (!stack.querySelector('.preview-link')) {
        const previewLink = document.createElement('a');
        previewLink.href = mainImage.src;
        previewLink.className = 'glightbox preview-link';
        previewLink.innerHTML = '<i class="bi bi-zoom-in"></i>';
        previewLink.title = stack.querySelector('.portfolio-info h4')?.textContent || 'Image Gallery';
        previewLink.dataset.gallery = `gallery-stack-${stackIndex}`;
        
        // Add to portfolio info section
        if (portfolioInfo) {
          portfolioInfo.appendChild(previewLink);
        }
      }

      // Create hidden gallery links for GLightbox
      const stackId = stack.getAttribute('data-stack-id') || `stack-${stackIndex}`;
      const galleryId = `gallery-${stackId}`;
      
      // Remove any existing gallery links first
      const existingGallery = stack.querySelector('.stack-gallery-links');
      if (existingGallery) {
        existingGallery.remove();
      }
      
      // Create new gallery links container
      const galleryLinksContainer = document.createElement('div');
      galleryLinksContainer.className = 'stack-gallery-links';
      galleryLinksContainer.style.display = 'none';
      
      // Add all images to the gallery
      stackData.forEach((imageUrl, i) => {
        const galleryLink = document.createElement('a');
        galleryLink.href = imageUrl;
        galleryLink.className = 'glightbox';
        galleryLink.dataset.gallery = galleryId;
        galleryLink.title = `${stack.querySelector('.portfolio-info h4')?.textContent || 'Image'} - ${i + 1}`;
        galleryLinksContainer.appendChild(galleryLink);
      });
      
      // Add gallery links to stack
      stack.appendChild(galleryLinksContainer);

      let currentIndex = 0;
      
      // Set total images
      if (totalImagesSpan) {
        totalImagesSpan.textContent = stackData.length;
      }
      
      // Function to update image
      function updateImage(index) {
        if (index < 0 || index >= stackData.length) return;
        
        currentIndex = index;
        mainImage.classList.add('loading');
        
        // Preload new image
        const newImg = new Image();
        newImg.onload = function() {
          mainImage.src = stackData[currentIndex];
          mainImage.classList.remove('loading');
          
          // Update the counter
          if (currentImageSpan) {
            currentImageSpan.textContent = currentIndex + 1;
          }

          // Update the preview link href
          const previewLink = stack.querySelector('.preview-link');
          if (previewLink) {
            previewLink.href = stackData[currentIndex];
          }
        };
        
        newImg.onerror = function() {
          mainImage.classList.remove('loading');
          console.error('Failed to load image:', stackData[currentIndex]);
        };
        
        newImg.src = stackData[currentIndex];
      }
      
      // Previous button click
      if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          const newIndex = currentIndex > 0 ? currentIndex - 1 : stackData.length - 1;
          updateImage(newIndex);
        });
      }
      
      // Next button click
      if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          const newIndex = currentIndex < stackData.length - 1 ? currentIndex + 1 : 0;
          updateImage(newIndex);
        });
      }
      
      // Make the entire stack clickable for next image (except when clicking on navigation buttons)
      stack.addEventListener('click', (e) => {
        // Don't trigger if clicking navigation buttons or links
        if (!e.target.closest('.stack-nav-btn') && !e.target.closest('a')) {
          const newIndex = currentIndex < stackData.length - 1 ? currentIndex + 1 : 0;
          updateImage(newIndex);
        }
      });
      
      // Keyboard navigation when focused
      stack.setAttribute('tabindex', '0'); // Make it focusable
      stack.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
          e.preventDefault();
          prevBtn.click();
        } else if (e.key === 'ArrowRight') {
          e.preventDefault();
          nextBtn.click();
        }
      });
      
      // Touch swipe support
      let touchStartX = 0;
      let touchEndX = 0;
      
      stack.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      });
      
      stack.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      });
      
      function handleSwipe() {
        const threshold = 50; // Minimum distance for a swipe
        
        if (touchEndX < touchStartX - threshold) {
          // Swipe left - next image
          const newIndex = currentIndex < stackData.length - 1 ? currentIndex + 1 : 0;
          updateImage(newIndex);
        }
        
        if (touchEndX > touchStartX + threshold) {
          // Swipe right - previous image
          const newIndex = currentIndex > 0 ? currentIndex - 1 : stackData.length - 1;
          updateImage(newIndex);
        }
      }
    });
  }

  window.addEventListener('load', function() {
    // Initialize GLightbox after image stacks are ready
    initImageStacks();
    
    if (typeof GLightbox === 'function') {
      const lightbox = GLightbox({
        selector: '.glightbox',
        touchNavigation: true,
        loop: true
      });
    }
  });

})();