import os

base = r"C:\Users\Shrushti\OneDrive\Desktop\pawan creative"

WA_BTN = '<a href="https://wa.me/918308513606" class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>'

SCRIPTS = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>\n<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/Flip.min.js"></script>\n<script src="https://unpkg.com/lenis@1.1.18/dist/lenis.min.js"></script>\n<script src="js/main.js"></script>'

def navbar(home_href="index.html", contact_href="#contact"):
    return f'''<nav class="navbar" id="navbar">
  <a href="index.html" class="navbar__brand">pawan creative space</a>
  <div class="navbar__links">
    <a href="index.html" class="nav-link" data-nav>Home</a>
    <a href="works.html" class="nav-link" data-nav>Works</a>
    <a href="about.html" class="nav-link" data-nav>About</a>
    <a href="process.html" class="nav-link" data-nav>Process</a>
    <a href="shop.html" class="nav-link" data-nav>Shop</a>
    <a href="{contact_href}" class="nav-link" data-nav>Contact</a>
    <span class="nav-divider"></span>
    <a href="https://www.instagram.com/pawan_creative_space" target="_blank" class="nav-link">Instagram</a>
  </div>
  <button class="navbar__menu-btn" id="menu-btn">menu</button>
</nav>
<div class="menu-overlay" id="menu-overlay">
  <button class="menu-overlay__close" id="menu-close">close</button>
  <div class="menu-overlay__links">
    <a href="index.html" class="menu-link">home</a>
    <a href="works.html" class="menu-link">works</a>
    <a href="about.html" class="menu-link">about</a>
    <a href="process.html" class="menu-link">process</a>
    <a href="shop.html" class="menu-link">shop</a>
    <a href="{contact_href}" class="menu-link">contact</a>
  </div>
  <div class="menu-overlay__social">
    <a href="https://www.instagram.com/pawan_creative_space" target="_blank">instagram</a>
    <a href="https://www.linkedin.com/in/pawan-creative-space-ba526b42a" target="_blank">linkedin</a>
    <a href="https://youtube.com/@pawancreativespace" target="_blank">youtube</a>
  </div>
</div>'''

def head(title, desc="Pawan Creative Space - Premium Interior Design. Your Dream, Our Design."):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <title>Pawan Creative Space | {title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600&amp;family=Inter:wght@300;400;500&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="grain"></div>
<div class="progress-bar" id="progress-bar"></div>'''

def foot():
    return f'''</main>
{WA_BTN}
{SCRIPTS}
</body>
</html>'''

# ─── INDEX ────────────────────────────────────────────────────────────────────
index = head("Your Dream, Our Design") + '''
<div class="loader" id="loader">
  <div class="loader__label loader__label--top">Your Dream, Our Design</div>
  <div class="loader__logo-wrap">
    <img src="logo.jpeg" alt="Pawan Creative Space" class="loader__logo" id="loader-logo">
  </div>
  <div class="loader__label loader__label--bottom">Pawan Creative Space</div>
</div>
''' + navbar(contact_href="#contact") + '''
<main id="smooth-content">
<section class="hero" id="hero">
  <div class="hero__slider">
    <div class="hero__col hero__col--left">
      <div class="hero__slide" data-slide="0"><img src="badroom blue.jpeg" alt="Blue Bedroom"></div>
      <div class="hero__slide" data-slide="1"><img src="badroom pink.jpeg" alt="Pink Bedroom"></div>
      <div class="hero__slide" data-slide="2"><img src="badroom yellow.jpeg" alt="Yellow Bedroom"></div>
      <div class="hero__slide" data-slide="3"><img src="badroom green.jpeg" alt="Green Bedroom"></div>
    </div>
    <div class="hero__col hero__col--right">
      <div class="hero__slide" data-slide="0"><img src="hall blue.jpeg" alt="Blue Hall"></div>
      <div class="hero__slide" data-slide="1"><img src="hall pink.jpeg" alt="Pink Hall"></div>
      <div class="hero__slide" data-slide="2"><img src="hall yellow.jpeg" alt="Yellow Hall"></div>
      <div class="hero__slide" data-slide="3"><img src="hall green.jpeg" alt="Green Hall"></div>
    </div>
    <div class="hero__labels">
      <div class="hero__label" data-slide="0" style="--accent: #7B9CB5"><div class="hero__label-inner"><h2>Blue Serenity</h2><span class="hero__label-cat">Bedroom &amp; Hall</span></div></div>
      <div class="hero__label" data-slide="1" style="--accent: #C4909A"><div class="hero__label-inner"><h2>Blush Elegance</h2><span class="hero__label-cat">Bedroom &amp; Hall</span></div></div>
      <div class="hero__label" data-slide="2" style="--accent: #C4A94D"><div class="hero__label-inner"><h2>Golden Warmth</h2><span class="hero__label-cat">Bedroom &amp; Hall</span></div></div>
      <div class="hero__label" data-slide="3" style="--accent: #7BA07B"><div class="hero__label-inner"><h2>Sage Harmony</h2><span class="hero__label-cat">Bedroom &amp; Hall</span></div></div>
    </div>
  </div>
  <div class="hero__tagline"><span class="star-icon">&#10022;</span><span>Your Dream, Our Design</span><span class="star-icon">&#10022;</span></div>
</section>
<section class="services" id="services">
  <div class="container">
    <div class="services__grid">
      <div class="services__text">
        <span class="section-label">What We Do</span>
        <h2 class="section-heading reveal-text">Crafting Spaces<br>That Inspire</h2>
        <p class="services__desc reveal-text">We compose thoughtful interior ecosystems, balancing volume, color, and light.<br>Every detail is engineered with precision, from concept sketches to execution.<br>Bespoke woodwork, customized modular planning, and hand-selected luxury textures.<br>Creating sanctuaries of quiet luxury since 2020 for refined contemporary living.</p>
        <div class="services__list">
          <div class="service-item"><span class="star-icon">&#10022;</span> Interior Designing</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Modular Kitchen</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Wardrobe Design</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> TV Unit</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> False Ceiling</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Acrylic Laminate Work</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Interior Furniture</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Colour &amp; Texture Painting</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Office Interior</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Renovation &amp; Remodeling</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> 2D &amp; 3D Design</div>
          <div class="service-item"><span class="star-icon">&#10022;</span> Space Planning</div>
        </div>
      </div>
      <div class="services__images">
        <div class="services__img-large reveal-img"><img src="hall green.jpeg" alt="Hall Interior"></div>
        <div class="services__img-small reveal-img"><img src="multi furniture 1.jpeg" alt="Furniture"></div>
      </div>
    </div>
  </div>
</section>
<section class="why-choose" id="why-choose">
  <div class="container"><h2 class="section-heading reveal-text">Why Choose Us</h2></div>
  <div class="why-choose__track-wrap"><div class="why-choose__track">
    <div class="value-card"><span class="value-card__num">01</span><h3>Premium Quality Material</h3><p>Only the finest materials selected for lasting elegance</p></div>
    <div class="value-card"><span class="value-card__num">02</span><h3>Customized Designs</h3><p>Every space tailored to your unique lifestyle and taste</p></div>
    <div class="value-card"><span class="value-card__num">03</span><h3>Transparent Pricing</h3><p>No hidden costs, clear detailed quotations always</p></div>
    <div class="value-card"><span class="value-card__num">04</span><h3>Experienced Team</h3><p>Skilled craftsmen and designers with years of expertise</p></div>
    <div class="value-card"><span class="value-card__num">05</span><h3>On-Time Delivery</h3><p>Projects completed within committed timelines</p></div>
    <div class="value-card"><span class="value-card__num">06</span><h3>Latest Design Trends</h3><p>Contemporary aesthetics rooted in timeless principles</p></div>
    <div class="value-card"><span class="value-card__num">07</span><h3>Professional Management</h3><p>End-to-end project coordination for a seamless experience</p></div>
    <div class="value-card"><span class="value-card__num">08</span><h3>Customer Satisfaction</h3><p>Your happiness is the true measure of our success</p></div>
  </div></div>
</section>
<section class="testimonials" id="testimonials">
  <div class="container">
    <div class="testimonials__quote-mark">&ldquo;</div>
    <blockquote class="testimonials__quote reveal-text">Pawan Creative Space transformed our home beyond our imagination. The attention to detail, quality of materials, and design sensibility were exceptional. They truly understood our vision.</blockquote>
    <cite class="testimonials__cite">&mdash; A Happy Homeowner</cite>
    <div class="testimonials__stats">
      <div class="stat"><span class="stat__num" data-target="150">0</span><span class="stat__plus">+</span><span class="stat__label">Happy Clients</span></div>
      <div class="stat"><span class="stat__num" data-target="200">0</span><span class="stat__plus">+</span><span class="stat__label">Projects Completed</span></div>
      <div class="stat"><span class="stat__num" data-target="2020">0</span><span class="stat__label">Since Started</span></div>
      <div class="stat"><span class="stat__num" data-target="100">0</span><span class="stat__plus">%</span><span class="stat__label">Customer Satisfaction</span></div>
    </div>
  </div>
</section>
<section class="contact" id="contact">
  <div class="container">
    <div class="contact__grid">
      <div class="contact__info">
        <h2 class="section-heading reveal-text">Let\'s Create<br>Something Beautiful</h2>
        <p class="contact__tagline reveal-text">We design spaces that tell your story. Complete interior solutions from modular setups to bespoke styling.</p>
        <div class="contact__grid-inner">
          <div class="contact__col"><h4>Quick Links</h4><div class="contact__links"><a href="works.html">Works</a><a href="about.html">About</a><a href="process.html">Process</a><a href="shop.html">Shop</a><a href="#contact">Contact</a></div></div>
          <div class="contact__col"><h4>Contact Info</h4><div class="contact__links"><a href="tel:8308513606">8308513606</a><a href="mailto:pgosavi2000@gmail.com">pgosavi2000@gmail.com</a></div></div>
          <div class="contact__col"><h4>Social Connect</h4><div class="contact__links"><a href="https://www.instagram.com/pawan_creative_space" target="_blank">Instagram</a><a href="https://www.linkedin.com/in/pawan-creative-space-ba526b42a" target="_blank">LinkedIn</a><a href="https://youtube.com/@pawancreativespace" target="_blank">YouTube</a></div></div>
        </div>
        <div class="contact__copyright"><span>&copy; 2025 Pawan Creative Space. All rights reserved.</span><span>Your Dream, Our Design</span></div>
      </div>
      <div class="contact__form-card">
        <h3 class="form-title">Start Your Project</h3>
        <form class="contact__form" id="contact-form">
          <div class="form-group"><label>Name</label><input type="text" name="name" placeholder="Your name" required></div>
          <div class="form-group"><label>Email</label><input type="email" name="email" placeholder="Your email" required></div>
          <div class="form-group"><label>Phone</label><input type="tel" name="phone" placeholder="Your phone number"></div>
          <div class="form-group"><label>Message</label><textarea name="message" placeholder="Tell us about your project" rows="4" required></textarea></div>
          <button type="submit" class="btn-submit">Send via WhatsApp &#9658;</button>
          <p class="form-note">We typically respond within 24 hours</p>
        </form>
      </div>
    </div>
  </div>
</section>
''' + foot()

# ─── WORKS ────────────────────────────────────────────────────────────────────
works = head("Our Work") + navbar(contact_href="index.html#contact") + '''
<main id="smooth-content">
<section class="works" id="works" style="padding-top:90px;">
  <div class="container">
    <span class="section-label">Portfolio</span>
    <h2 class="section-heading reveal-text">Our Work</h2>
    <div class="section-wa-container"><a href="https://wa.me/918308513606?text=I%27m%20interested%20in%20your%20work%20portfolio" class="btn-wa" target="_blank">&#128172; Chat on WhatsApp</a></div>
  </div>
  <div class="works__grid" id="works-grid">
    <div class="works__item"><img src="work 1.jpeg" alt="Work 1"><div class="works__item-info"><h3>Modern Living Room</h3><span>Residential</span></div></div>
    <div class="works__item"><img src="work 2.jpeg" alt="Work 2"><div class="works__item-info"><h3>Contemporary Kitchen</h3><span>Kitchen Design</span></div></div>
    <div class="works__item"><img src="work 3.jpeg" alt="Work 3"><div class="works__item-info"><h3>Elegant Bedroom</h3><span>Bedroom Design</span></div></div>
    <div class="works__item"><img src="work 4.jpeg" alt="Work 4"><div class="works__item-info"><h3>Premium Interior</h3><span>Residential</span></div></div>
    <div class="works__item"><img src="work 5.jpeg" alt="Work 5"><div class="works__item-info"><h3>Nature Inspired</h3><span>Bedroom Design</span></div></div>
    <div class="works__item"><img src="work 6.jpeg" alt="Work 6"><div class="works__item-info"><h3>Warm Elegance</h3><span>Residential</span></div></div>
  </div>
  <div class="works__video container">
    <span class="section-label">Before &amp; After</span>
    <h3 class="reveal-text">See the Transformation</h3>
    <div class="works__video-frame">
      <video src="video before after.mp4" muted loop playsinline id="works-video"></video>
      <div class="works__video-play" id="video-play">&#9654; Play</div>
    </div>
  </div>
</section>
''' + foot()

# ─── ABOUT ────────────────────────────────────────────────────────────────────
about = head("About Us") + navbar(contact_href="index.html#contact") + '''
<main id="smooth-content">
<section class="about" id="about" style="padding-top:60px;">
  <div class="about__hero">
    <div class="about__hero-img reveal-img"><img src="hall green.jpeg" alt="Interior Design"></div>
    <div class="about__hero-frame"></div>
  </div>
  <div class="container">
    <h2 class="section-heading reveal-text">Elegant Interiors,<br>Crafted With Purpose</h2>
    <div class="section-wa-container"><a href="https://wa.me/918308513606?text=I%27d%20like%20to%20know%20more%20about%20Pawan%20Creative%20Space" class="btn-wa" target="_blank">&#128172; Chat on WhatsApp</a></div>
    <div class="about__content">
      <div class="about__text">
        <p class="about__desc">At Pawan Creative Space, we specialize in creating elegant and functional interior spaces for homes. We deliver complete interior solutions with quality craftsmanship, modern designs, and timely project completion.</p>
        <div class="about__blocks">
          <div class="about__block"><h4>Our Mission</h4><p>To transform every space into a beautiful, functional, and inspiring environment. We are committed to delivering innovative interior design solutions that reflect our clients\' lifestyle, vision, and budget.</p></div>
          <div class="about__block"><h4>Our Vision</h4><p>To become one of the most trusted and preferred interior design companies, recognized for creativity, quality, innovation, and exceptional customer service.</p></div>
          <div class="about__block"><h4>Quality Commitment</h4><p>From selecting premium materials to ensuring precise execution, we maintain the highest standards throughout every stage of the project.</p></div>
        </div>
      </div>
      <div class="about__founder">
        <div class="about__founder-img reveal-img"><img src="founder.jpeg" alt="Pawan Gosavi"></div>
        <h3>Pawan Gosavi</h3>
        <span class="section-label">Founder &amp; Creative Director</span>
      </div>
    </div>
  </div>
  <div class="about__cta">
    <a href="index.html#contact" class="about__cta-link">
      <span class="about__cta-text">Let\'s</span>
      <div class="about__cta-video"><video src="video bg.mp4" muted loop autoplay playsinline></video></div>
      <span class="about__cta-text">Talk</span>
    </a>
  </div>
</section>
''' + foot()

# ─── PROCESS ──────────────────────────────────────────────────────────────────
process = head("Our Process") + navbar(contact_href="index.html#contact") + '''
<main id="smooth-content">
<section class="process" id="process">
  <div class="process__hero">
    <div class="process__hero-img"><img src="multi furniture 1.jpeg" alt="Process"></div>
    <h2 class="process__title reveal-text">Process</h2>
  </div>
  <div class="process__label-bar">
    <span>Our step-by-step approach &nbsp;&nbsp;</span>
    <a href="https://wa.me/918308513606?text=I%27m%20interested%20in%20your%20design%20process" class="btn-wa" target="_blank" style="font-size:0.72rem;display:inline-flex">&#128172; WhatsApp</a>
  </div>
  <div class="process__steps">
    <div class="process__step" data-step="1">
      <div class="process__step-bg"><img src="multi furniture 1.jpeg" alt=""></div>
      <div class="process__step-content"><div class="process__step-num">01</div><h3>Consultation</h3><p>We begin by listening. Understanding your needs, lifestyle, and vision for the space.</p></div>
      <div class="process__step-img reveal-img"><img src="Consultation.jpg" alt="Consultation"></div>
    </div>
    <div class="process__step" data-step="2">
      <div class="process__step-bg"><img src="multi furniture 2.jpeg" alt=""></div>
      <div class="process__step-content"><div class="process__step-num">02</div><h3>Site Visit</h3><p>Our team visits the location to assess dimensions, natural light, ventilation, and structural elements.</p></div>
      <div class="process__step-img reveal-img"><img src="Site Visit.jpeg" alt="Site Visit"></div>
    </div>
    <div class="process__step" data-step="3">
      <div class="process__step-bg"><img src="multi furniture 3.jpeg" alt=""></div>
      <div class="process__step-content"><div class="process__step-num">03</div><h3>Design Planning</h3><p>We translate your brief into clear architectural intentions - layouts, flow, and spatial logic.</p></div>
      <div class="process__step-img reveal-img"><img src="design planning-1.jpeg" alt="Design Planning"></div>
    </div>
    <div class="process__step" data-step="4">
      <div class="process__step-bg"><img src="multi furniture 4.jpeg" alt=""></div>
      <div class="process__step-content"><div class="process__step-num">04</div><h3>2D &amp; 3D Design</h3><p>Detailed floor plans, elevations, and photorealistic 3D renders bring the concept to life.</p></div>
      <div class="process__step-img reveal-img"><img src="design 2d 3d.png" alt="2D 3D Design"></div>
    </div>
    <div class="process__step" data-step="5">
      <div class="process__step-bg"><img src="multi furniture 1.jpeg" alt=""></div>
      <div class="process__step-content"><div class="process__step-num">05</div><h3>Material Selection</h3><p>We curate premium materials, textures, and finishes that define the character of your space.</p></div>
      <div class="process__step-img reveal-img"><img src="Material Selection.jpeg" alt="Material Selection"></div>
    </div>
    <div class="process__step" data-step="6">
      <div class="process__step-bg"><img src="multi furniture 2.jpeg" alt=""></div>
      <div class="process__step-content"><div class="process__step-num">06</div><h3>Final Handover</h3><p>Your dream space is delivered - polished, complete, and ready to be lived in.</p></div>
      <div class="process__step-img reveal-img"><img src="Final Handover.jpeg" alt="Final Handover"></div>
    </div>
  </div>
</section>
''' + foot()

# ─── SHOP ─────────────────────────────────────────────────────────────────────
furniture_imgs = "\n".join([f'      <img src="furniture {i}.jpeg" alt="" loading="lazy">' for i in range(1,22)])
shop = head("Shop / Furniture") + navbar(contact_href="index.html#contact") + f'''
<main id="smooth-content">
<section class="shop" id="shop" style="padding-top:80px;">
  <div class="container">
    <span class="section-label">Curated Collection</span>
    <h2 class="section-heading reveal-text">Curated Furniture</h2>
    <p class="shop__subtitle">Premium pieces selected for modern Indian homes</p>
    <div class="section-wa-container" style="justify-content:center"><a href="https://wa.me/918308513606?text=I%27m%20interested%20in%20your%20furniture%20collection" class="btn-wa" target="_blank">&#128172; Chat on WhatsApp</a></div>
  </div>
  <div class="shop__trail" id="shop-trail">
    <div class="shop__center-text"><span>Furniture</span><span class="shop__dot">&#10022;</span><span>Collection</span></div>
  </div>
  <div class="shop__marquee">
    <div class="shop__marquee-track">
{furniture_imgs}
{furniture_imgs}
    </div>
  </div>
  <div class="container" style="text-align:center; padding-top: 3rem;">
    <a href="index.html#contact" class="btn-pill">Contact Us to Buy Furniture &#9658;</a>
  </div>
</section>
''' + foot()

pages = {
    "index.html": index,
    "works.html": works,
    "about.html": about,
    "process.html": process,
    "shop.html": shop,
}

for fname, content in pages.items():
    path = os.path.join(base, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {fname} ({len(content)} chars)")

print("ALL DONE")
