// Register GSAP plugins
gsap.registerPlugin(ScrollTrigger, Flip);

let lenis; // Global lenis instance

// 1. INITIALIZATION
document.addEventListener('DOMContentLoaded', () => {
  initLenis();
  if (document.fonts) {
    document.fonts.ready.then(() => {
      initLoader();
    });
  } else {
    initLoader();
  }
});

// 2. LENIS SMOOTH SCROLL
function initLenis() {
  if (typeof Lenis !== 'undefined') {
    lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t))
    });

    lenis.on('scroll', ScrollTrigger.update);

    gsap.ticker.add((time) => {
      lenis.raf(time * 1000);
    });

    gsap.ticker.lagSmoothing(0);
    lenis.stop(); // Stop scrolling until loader completes
  }
}

// 4. LOADER ANIMATION (initLoader)
function initLoader() {
  const loader = document.querySelector('.loader');
  if (!loader) {
    if (lenis) lenis.start();
    initAllAnimations();
    return;
  }

  const tl = gsap.timeline();

  gsap.set('body', { overflow: 'hidden' });

  // 1. Simple fade in and slight scale up for the logo
  tl.fromTo('.loader__logo-wrap',
    { opacity: 0, scale: 0.95 },
    { opacity: 1, scale: 1, duration: 1.0, ease: 'power2.out' }
  );

  // 2. Hold for a moment
  tl.to({}, { duration: 1.0 });

  // 3. Fade out logo
  tl.to('.loader__logo-wrap', {
    opacity: 0, duration: 0.5, ease: 'power2.inOut'
  });

  // 4. Fade out loader screen
  tl.to('.loader', {
    opacity: 0,
    duration: 0.5,
    ease: 'power2.inOut',
    onComplete: () => {
      loader.style.display = 'none';
      gsap.set('body', { overflow: '' });
      if (lenis) lenis.start();
      initAllAnimations();
    }
  });
}

// 5. NAVBAR SCROLL BEHAVIOR
function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;
  
  let lastScroll = 0;
  
  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;
    // Add scrolled class after 50px
    navbar.classList.toggle('scrolled', currentScroll > 50);
    // Hide on scroll down, show on scroll up
    if (currentScroll > lastScroll && currentScroll > 100) {
      navbar.classList.add('hidden');
    } else {
      navbar.classList.remove('hidden');
    }
    lastScroll = currentScroll;
  });
  
  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      e.preventDefault();
      const href = anchor.getAttribute('href');
      if (href === '#') return;
      
      const target = document.querySelector(href);
      if (target && lenis) {
        lenis.scrollTo(target, { offset: -60 });
      }
      // Close mobile menu if open
      const menuOverlay = document.getElementById('menu-overlay');
      if (menuOverlay) menuOverlay.classList.remove('active');
    });
  });
  
  // Mobile menu
  const menuBtn = document.getElementById('menu-btn');
  const menuClose = document.getElementById('menu-close');
  const menuOverlay = document.getElementById('menu-overlay');
  
  if (menuBtn && menuOverlay) {
    menuBtn.addEventListener('click', () => {
      menuOverlay.classList.add('active');
    });
  }
  if (menuClose && menuOverlay) {
    menuClose.addEventListener('click', () => {
      menuOverlay.classList.remove('active');
    });
  }
  
  // Stagger nav links in
  gsap.from('.nav-link', { 
    opacity: 0, 
    x: 20, 
    stagger: 0.05, 
    duration: 0.6, 
    ease: 'power2.out', 
    delay: 0.5 
  });
}

// 6. HERO SPLIT-SCREEN SLIDER
function initHeroSlider() {
  const heroSection = document.querySelector('.hero');
  if (!heroSection) return;
  
  const slides = 4;
  const leftSlides = heroSection.querySelectorAll('.hero__col--left .hero__slide');
  const rightSlides = heroSection.querySelectorAll('.hero__col--right .hero__slide');
  const labels = heroSection.querySelectorAll('.hero__label');
  
  if (!leftSlides.length || !rightSlides.length) return;

  ScrollTrigger.create({
    trigger: '.hero',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 0.5,
    onUpdate: (self) => {
      const progress = self.progress;
      const totalSlides = slides;
      const slideProgress = progress * (totalSlides - 1);
      const currentIndex = Math.floor(slideProgress);
      const t = slideProgress - currentIndex; // 0 to 1 between slides
      
      // Update all slides
      for (let i = 0; i < totalSlides; i++) {
        if (i < currentIndex) {
          // Already passed - fully visible
          if (leftSlides[i]) leftSlides[i].style.clipPath = 'inset(0 0 0 0)';
          if (rightSlides[i]) rightSlides[i].style.clipPath = 'inset(0 0 0 0)';
          if (labels[i]) labels[i].style.opacity = '0';
        } else if (i === currentIndex) {
          // Current - fully visible
          if (leftSlides[i]) leftSlides[i].style.clipPath = 'inset(0 0 0 0)';
          if (rightSlides[i]) rightSlides[i].style.clipPath = 'inset(0 0 0 0)';
          if (labels[i]) labels[i].style.opacity = `${1 - t}`;
        } else if (i === currentIndex + 1) {
          // Next - revealing
          const insetValue = (1 - t) * 100;
          if (leftSlides[i]) leftSlides[i].style.clipPath = `inset(${insetValue}% 0 0 0)`;
          if (rightSlides[i]) rightSlides[i].style.clipPath = `inset(0 0 ${insetValue}% 0)`;
          if (labels[i]) labels[i].style.opacity = `${t}`;
        } else {
          // Future - hidden
          if (leftSlides[i]) leftSlides[i].style.clipPath = 'inset(100% 0 0 0)';
          if (rightSlides[i]) rightSlides[i].style.clipPath = 'inset(0 0 100% 0)';
          if (labels[i]) labels[i].style.opacity = '0';
        }
      }
    }
  });
}

// 7. TEXT REVEAL ANIMATION (Custom SplitText replacement)
function initTextReveals() {
  document.querySelectorAll('.reveal-text').forEach(el => {
    // Split text into individual characters wrapped in overflow-hidden spans
    const originalHTML = el.innerHTML;
    const lines = originalHTML.split('<br>');
    el.innerHTML = '';
    
    lines.forEach((line, lineIndex) => {
      if (lineIndex > 0) el.appendChild(document.createElement('br'));
      const lineText = line.replace(/<[^>]*>/g, '').trim();
      lineText.split('').forEach(char => {
        const wrapper = document.createElement('span');
        wrapper.style.display = 'inline-block';
        wrapper.style.overflow = 'hidden';
        wrapper.style.verticalAlign = 'top';
        
        const charSpan = document.createElement('span');
        charSpan.style.display = 'inline-block';
        charSpan.style.transform = 'translateY(110%)';
        charSpan.textContent = char === ' ' ? '\u00A0' : char;
        charSpan.className = 'split-char';
        
        wrapper.appendChild(charSpan);
        el.appendChild(wrapper);
      });
    });
    
    // Replay animation every time the element enters viewport
    ScrollTrigger.create({
      trigger: el,
      start: 'top 85%',
      end: 'bottom 10%',
      onEnter: () => {
        gsap.to(el.querySelectorAll('.split-char'), {
          y: 0, duration: 0.8, stagger: 0.02, ease: 'expo.out'
        });
      },
      onLeave: () => {
        gsap.set(el.querySelectorAll('.split-char'), { y: '110%' });
      },
      onEnterBack: () => {
        gsap.to(el.querySelectorAll('.split-char'), {
          y: 0, duration: 0.8, stagger: 0.02, ease: 'expo.out'
        });
      },
      onLeaveBack: () => {
        gsap.set(el.querySelectorAll('.split-char'), { y: '110%' });
      }
    });
  });
}

// 8. IMAGE REVEALS
function initImageReveals() {
  document.querySelectorAll('.reveal-img').forEach(el => {
    gsap.set(el, { clipPath: 'inset(100% 0 0 0)' });
    ScrollTrigger.create({
      trigger: el,
      start: 'top 85%',
      end: 'bottom 10%',
      onEnter: () => {
        gsap.to(el, { clipPath: 'inset(0 0 0 0)', duration: 1.2, ease: 'expo.inOut' });
      },
      onLeave: () => {
        gsap.set(el, { clipPath: 'inset(0 0 100% 0)' });
      },
      onEnterBack: () => {
        gsap.to(el, { clipPath: 'inset(0 0 0 0)', duration: 1.2, ease: 'expo.inOut' });
      },
      onLeaveBack: () => {
        gsap.set(el, { clipPath: 'inset(100% 0 0 0)' });
      }
    });
  });
}

// 9. SERVICES ANIMATION
function initServices() {
  const serviceItems = document.querySelectorAll('.service-item');
  if (serviceItems.length > 0) {
    gsap.set(serviceItems, { y: 30, opacity: 0 });
    ScrollTrigger.create({
      trigger: '.services__list',
      start: 'top 80%',
      end: 'bottom 10%',
      onEnter: () => gsap.to(serviceItems, { y: 0, opacity: 1, stagger: 0.05, duration: 0.6, ease: 'power2.out' }),
      onLeave: () => gsap.set(serviceItems, { y: -30, opacity: 0 }),
      onEnterBack: () => gsap.to(serviceItems, { y: 0, opacity: 1, stagger: 0.05, duration: 0.6, ease: 'power2.out' }),
      onLeaveBack: () => gsap.set(serviceItems, { y: 30, opacity: 0 })
    });
  }
}

// 9.5 AMAZING ZOOM SECTION
function initZoom() {
  const zoomSection = document.querySelector('.zoom-section');
  if (!zoomSection) return;
  
  gsap.fromTo('.zoom-img', 
    { width: '20vw', height: '30vh', borderRadius: '20px' },
    { 
      width: '150vw', height: '150vh', borderRadius: '0px',
      ease: 'none',
      scrollTrigger: {
        trigger: zoomSection,
        start: 'top top',
        end: '+=150%',
        scrub: true,
        pin: true
      }
    }
  );
  gsap.fromTo('.zoom-text', 
    { scale: 0.8, opacity: 0 },
    { 
      scale: 1, opacity: 1,
      ease: 'none',
      scrollTrigger: {
        trigger: zoomSection,
        start: 'top top',
        end: '+=50%',
        scrub: true
      }
    }
  );
}

// 10. WHY CHOOSE US - HORIZONTAL SCROLL (Desktop) / Stack (Mobile)
function initWhyChoose() {
  const track = document.querySelector('.why-choose__track');
  if (!track) return;

  // Always make cards visible first
  const cards = document.querySelectorAll('.value-card');
  gsap.set(cards, { opacity: 1, scale: 1, clearProps: 'all' });

  const isMobile = window.innerWidth <= 1024;
  if (isMobile) return; // On mobile/tablet, just show as stacked

  const getScrollAmount = () => -(track.scrollWidth - window.innerWidth + 100);

  const tween = gsap.to(track, {
    x: getScrollAmount,
    ease: 'none',
    paused: true
  });

  ScrollTrigger.create({
    trigger: '.why-choose',
    start: 'top top',
    end: () => `+=${Math.abs(getScrollAmount())}`,
    pin: true,
    animation: tween,
    scrub: 1.2,
    invalidateOnRefresh: true,
    onRefresh: () => gsap.set(cards, { opacity: 1, clearProps: 'all' })
  });
}

// 11. WORKS - GRID ANIMATION
function initWorks() {
  const items = document.querySelectorAll('.works__item-adv');
  if (items.length > 0) {
    gsap.set(items, { y: 60, opacity: 0 });
    ScrollTrigger.create({
      trigger: '.works__grid-advanced',
      start: 'top 80%',
      end: 'bottom 10%',
      onEnter: () => gsap.to(items, { y: 0, opacity: 1, stagger: 0.1, duration: 0.8, ease: 'power2.out' }),
      onLeave: () => gsap.set(items, { y: -60, opacity: 0 }),
      onEnterBack: () => gsap.to(items, { y: 0, opacity: 1, stagger: 0.1, duration: 0.8, ease: 'power2.out' }),
      onLeaveBack: () => gsap.set(items, { y: 60, opacity: 0 })
    });
  }
  
  // Video play/pause
  const video = document.getElementById('works-video');
  const playBtn = document.getElementById('video-play');
  if (video && playBtn) {
    playBtn.addEventListener('click', () => {
      if (video.paused) {
        video.play();
        playBtn.textContent = '⏸ Pause';
      } else {
        video.pause();
        playBtn.textContent = '▶ Play';
      }
    });
  }
}

// 12. ABOUT SECTION
function initAbout() {
  // Parallax hero image
  if (document.querySelector('.about__hero-img img')) {
    gsap.to('.about__hero-img img', {
      scale: 1,
      ease: 'none',
      scrollTrigger: {
        trigger: '.about__hero',
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    });
  }
  
  // Stagger text blocks
  const blocks = document.querySelectorAll('.about__block');
  if (blocks.length > 0) {
    gsap.set(blocks, { y: 40, opacity: 0 });
    ScrollTrigger.create({
      trigger: '.about__content',
      start: 'top 80%',
      end: 'bottom 10%',
      onEnter: () => gsap.to(blocks, { y: 0, opacity: 1, stagger: 0.15, duration: 0.8, ease: 'power2.out' }),
      onLeave: () => gsap.set(blocks, { y: -40, opacity: 0 }),
      onEnterBack: () => gsap.to(blocks, { y: 0, opacity: 1, stagger: 0.15, duration: 0.8, ease: 'power2.out' }),
      onLeaveBack: () => gsap.set(blocks, { y: 40, opacity: 0 })
    });
  }
  
  const desc = document.querySelector('.about__desc');
  if (desc) {
    gsap.set(desc, { y: 30, opacity: 0 });
    ScrollTrigger.create({
      trigger: desc,
      start: 'top 85%',
      end: 'bottom 10%',
      onEnter: () => gsap.to(desc, { y: 0, opacity: 1, duration: 0.8, ease: 'power2.out' }),
      onLeave: () => gsap.set(desc, { y: -30, opacity: 0 }),
      onEnterBack: () => gsap.to(desc, { y: 0, opacity: 1, duration: 0.8, ease: 'power2.out' }),
      onLeaveBack: () => gsap.set(desc, { y: 30, opacity: 0 })
    });
  }
}

// 13. PROCESS SECTION
function initProcess() {
  const steps = document.querySelectorAll('.process__step');
  steps.forEach(step => {
    const content = step.querySelector('.process__step-content');
    if (content) {
      gsap.set(content, { x: -50, opacity: 0 });
      ScrollTrigger.create({
        trigger: step,
        start: 'top 70%',
        end: 'bottom 10%',
        onEnter: () => gsap.to(content, { x: 0, opacity: 1, duration: 0.8, ease: 'power2.out' }),
        onLeave: () => gsap.set(content, { x: 50, opacity: 0 }),
        onEnterBack: () => gsap.to(content, { x: 0, opacity: 1, duration: 0.8, ease: 'power2.out' }),
        onLeaveBack: () => gsap.set(content, { x: -50, opacity: 0 })
      });
    }
    
    const img = step.querySelector('.process__step-img');
    if (img) {
      gsap.set(img, { clipPath: 'inset(100% 0 0 0)' });
      ScrollTrigger.create({
        trigger: step,
        start: 'top 60%',
        end: 'bottom 10%',
        onEnter: () => gsap.to(img, { clipPath: 'inset(0 0 0 0)', duration: 1.2, ease: 'expo.inOut' }),
        onLeave: () => gsap.set(img, { clipPath: 'inset(0 0 100% 0)' }),
        onEnterBack: () => gsap.to(img, { clipPath: 'inset(0 0 0 0)', duration: 1.2, ease: 'expo.inOut' }),
        onLeaveBack: () => gsap.set(img, { clipPath: 'inset(100% 0 0 0)' })
      });
    }
  });
}

// 14. SHOP - MOUSE TRAIL (also works on mobile via touch)
function initShopTrail() {
  const trailArea = document.getElementById('shop-trail');
  if (!trailArea) return;
  
  const furnitureImages = [];
  for (let i = 1; i <= 21; i++) {
    furnitureImages.push(`furniture ${i}.jpeg`);
  }
  
  let imageIndex = 0;
  let lastX = 0, lastY = 0;
  const threshold = 80; // minimum distance before spawning new image
  
  function spawnImage(clientX, clientY) {
    const rect = trailArea.getBoundingClientRect();
    const x = clientX - rect.left;
    const y = clientY - rect.top;
    
    // keep within bounds
    if (x < 0 || y < 0 || x > rect.width || y > rect.height) return;
    
    const dist = Math.sqrt((x - lastX) ** 2 + (y - lastY) ** 2);
    if (dist < threshold) return;
    lastX = x; lastY = y;
    
    const img = document.createElement('img');
    img.src = furnitureImages[imageIndex % furnitureImages.length];
    img.className = 'shop__trail-img';
    img.style.position = 'absolute';
    img.style.pointerEvents = 'none';
    img.style.left = `${x - 90}px`;
    img.style.top = `${y - 115}px`;
    img.style.transform = `rotate(${(Math.random() - 0.5) * 10}deg) scale(0.5)`;
    img.style.opacity = '0';
    img.style.zIndex = '10';
    
    trailArea.appendChild(img);
    imageIndex++;
    
    gsap.to(img, { scale: 1, opacity: 1, duration: 0.3, ease: 'power2.out' });
    gsap.to(img, {
      opacity: 0, scale: 0.8, duration: 0.5, delay: 1.5,
      ease: 'power2.in', onComplete: () => img.remove()
    });
    
    // Limit max visible to avoid performance drops
    const trailImgs = trailArea.querySelectorAll('.shop__trail-img');
    if (trailImgs.length > 15) {
      gsap.to(trailImgs[0], { opacity: 0, duration: 0.2, onComplete: () => trailImgs[0].remove() });
    }
  }

  // Mouse support (desktop)
  trailArea.addEventListener('mousemove', (e) => {
    spawnImage(e.clientX, e.clientY);
  });

  // Touch support (mobile)
  trailArea.addEventListener('touchmove', (e) => {
    e.preventDefault();
    const touch = e.touches[0];
    spawnImage(touch.clientX, touch.clientY);
  }, { passive: false });
}

// 15. TESTIMONIALS - COUNTER ANIMATION & REVIEWS
function initTestimonials() {
  const reviewCards = document.querySelectorAll('.review-card');
  if (reviewCards.length > 0) {
    gsap.set(reviewCards, { y: 40, opacity: 0 });
    ScrollTrigger.create({
      trigger: '.testimonials__grid',
      start: 'top 85%',
      end: 'bottom 10%',
      onEnter: () => gsap.to(reviewCards, { y: 0, opacity: 1, stagger: 0.1, duration: 0.8, ease: 'power2.out' }),
      onLeave: () => gsap.set(reviewCards, { y: -40, opacity: 0 }),
      onEnterBack: () => gsap.to(reviewCards, { y: 0, opacity: 1, stagger: 0.1, duration: 0.8, ease: 'power2.out' }),
      onLeaveBack: () => gsap.set(reviewCards, { y: 40, opacity: 0 })
    });
  }

  document.querySelectorAll('.stat__num').forEach(el => {
    const target = parseInt(el.dataset.target) || 0;
    if (target === 0) return;
    
    ScrollTrigger.create({
      trigger: el,
      start: 'top 85%',
      end: 'bottom 10%',
      onEnter: () => {
        gsap.to({ val: 0 }, {
          val: target,
          duration: 2,
          ease: 'power2.out',
          onUpdate: function() { 
            el.textContent = Math.round(this.targets()[0].val); 
          }
        });
      },
      onLeaveBack: () => {
        el.textContent = '0'; // Reset when scrolled up
      }
    });
  });
}

// 16. CONTACT FORM ANIMATION
function initContact() {
  // Keep all contact content always visible - no hidden animations
  gsap.set(['.contact__detail', '.contact__form-card', '.contact__tagline', '.contact__col', '.contact__links a'], {
    opacity: 1, clearProps: 'all'
  });

  // Subtle entrance only for form card (no clip-path)
  const formCard = document.querySelector('.contact__form-card');
  if (formCard) {
    gsap.fromTo(formCard,
      { y: 30, opacity: 0 },
      {
        y: 0, opacity: 1, duration: 1, ease: 'power2.out',
        scrollTrigger: { trigger: formCard, start: 'top 90%', once: true }
      }
    );
  }

  const details = document.querySelectorAll('.contact__detail');
  if (details.length > 0) {
    gsap.fromTo(details,
      { y: 20, opacity: 0 },
      {
        y: 0, opacity: 1, stagger: 0.08, duration: 0.8, ease: 'power2.out',
        scrollTrigger: { trigger: '.contact__details', start: 'top 90%', once: true }
      }
    );
  }

}

function initProgressBar() {
  const bar = document.getElementById('progress-bar');
  if (!bar) return;
  
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const docHeight = Math.max(
      document.body.scrollHeight, document.documentElement.scrollHeight,
      document.body.offsetHeight, document.documentElement.offsetHeight,
      document.body.clientHeight, document.documentElement.clientHeight
    ) - window.innerHeight;
    
    if (docHeight > 0) {
      bar.style.width = `${(scrollTop / docHeight) * 100}%`;
    }
  });
}

// 18. MASTER INIT FUNCTION
function initAllAnimations() {
  initNavbar();
  initHeroSlider();
  initTextReveals();
  initImageReveals();
  initServices();
  initZoom();
  initWhyChoose();
  initWorks();
  initAbout();
  initProcess();
  initShopTrail();
  initTestimonials();
  initContact();
  initCTA();
  initProgressBar();
}


// SECTION BREAK LOADER (EXIT TRANSITION)
document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('a');
  links.forEach(link => {
    link.addEventListener('click', function(e) {
      const target = this.getAttribute('href');
      if (!target || target.startsWith('#') || target.includes('#') || this.target === '_blank') return;
      
      if (this.hostname === window.location.hostname) {
        e.preventDefault();
        const loader = document.querySelector('.loader');
        if (loader) {
          loader.style.display = 'flex';
          gsap.to(loader, { opacity: 1, duration: 0.5, onComplete: () => { window.location.href = target; } });
        } else {
          window.location.href = target;
        }
      }
    });
  });
});
