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

      // Handle thumbnail errors
      document.querySelectorAll('.portfolio-content img').forEach(img => {
        img.addEventListener('error', function() {
          // If thumbnail fails to load, use category-specific fallback
          const portfolioItem = this.closest('.portfolio-item');
          if (portfolioItem.classList.contains('videography')) {
            this.src = "/static/img/misc/misc-square-13.webp";
          } else if (portfolioItem.classList.contains('live-streaming')) {
            this.src = "/static/img/misc/misc-square-6.webp";
          } else {
            this.src = "/static/img/misc/misc-square-16.webp";
          }
        });
      });

      // Pause videos when clicking away
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
          // Stop propagation to prevent triggering iframe clicks
          event.stopPropagation();
        });
      });
      
      // Enable pointer events on iframe only when directly clicking on it
      document.querySelectorAll('.portfolio-content.video-embed').forEach(content => {
        content.addEventListener('click', function(event) {
          // Check if we're clicking on the iframe directly
          if (event.target.tagName.toLowerCase() === 'iframe') {
            event.target.style.pointerEvents = 'auto';
          }
        });
      });
    }
  }

  window.addEventListener('load', initPortfolio);

})();