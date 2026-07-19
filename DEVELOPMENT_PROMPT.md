# AI Website Development Prompt — KAWA'S Café (Django)

You are a **Senior Full-Stack Django Developer**, **UI/UX Designer**, **Solution Architect**, and **SEO Expert**.

Your task is to build a **production-ready**, **premium**, **high-performance**, **mobile-first**, **SEO-optimized** website for **KAWA'S Café**.

The website should feel less like a typical Kenyan café website and more like a **luxury café experience found in Dubai, Doha, or Istanbul**, while still embracing the relaxed coastal atmosphere of **Nyali, Mombasa**.

The entire project must follow modern Django best practices, clean architecture, reusable components, and scalable code.

---

# PROJECT INFORMATION

## Business Name

KAWA'S Café

---

## Industry

Premium Café

Specialty Coffee

Artisan Desserts

Breakfast

Fresh Juices

Matcha

Milkshakes

Mocktails

---

## Location

Mount Kenya Road

Nyali

Mombasa

Kenya

---

## Contact

Phone / WhatsApp

+254 119 000 999

---

## Social Media

Facebook

Instagram

TikTok

@kawa_ske

---

## Website

https://kawas.co.ke

---

# PROJECT STATUS

The Django project has already been created.

Project Name

```
kawas
```

PostgreSQL has already been configured.

Database

```
kawas
```

The next task is to **create all Django applications**, configure them correctly, and begin implementing the website.

---

# PRIMARY OBJECTIVE

Develop a premium Halal Café website that communicates:

- Luxury
- Hospitality
- Warmth
- Simplicity
- Premium Coffee
- Modern Lifestyle
- Family Friendly
- Coastal Elegance

The website should convert visitors into café customers while showcasing KAWA'S products beautifully.

---

# DESIGN DIRECTION

The design inspiration should come from:

- Apple
- % Arabica
- Bateel Café
- EL&N London
- Premium Dubai Cafés
- Turkish Coffee Houses

NOT

❌ Fast food

❌ Generic restaurant templates

❌ Cheap WordPress themes

---

# BRAND PERSONALITY

KAWA'S is:

☕

Premium Specialty Coffee

🌙

Halal Certified

🍰

Luxury Desserts

🌴

Coastal Lifestyle

✨

Instagram Worthy

🤎

Warm Hospitality

👨‍👩‍👧‍👦

Family Friendly

💻

Modern Workspace

---

# TARGET AUDIENCE

- Coffee lovers
- Young professionals
- Students
- Families
- Tourists
- Digital nomads
- Muslim families
- Gen-Z
- Millennials

Age

18–40

---

# BRAND COLORS

Primary

```
#3E2723
```

Deep Espresso Brown

---

Secondary

```
#F5E6D3
```

Warm Latte Sand

---

Accent

```
#D4A94A
```

Honey Amber Gold

---

Supporting

```
#FFFFFF
```

```
#1A1A1A
```

```
#8A9A5B
```

Use Sage ONLY for:

- Halal Certified
- Fresh Ingredients
- Organic
- Alcohol-Free

---

# TYPOGRAPHY

Headings

Fraunces

Fallback

Cormorant Garamond

---

Body

Plus Jakarta Sans

Fallback

Inter

---

Arabic Support

Noto Naskh Arabic

---

# UI STYLE

Modern

Luxury

Minimal

Warm

Soft

Premium

Large spacing

Rounded corners

Glassmorphism (subtle)

Elegant animations

Excellent mobile experience

---

# ICONS

Use

Lucide Icons

Only

---

# RESPONSIVENESS

Mobile-first

320px+

Tablet

Desktop

Ultra-wide

Everything must be perfectly responsive.

---

# ANIMATIONS

Use subtle animations only.

Examples:

- Fade in
- Lift on hover
- Image zoom
- Coffee steam
- Smooth transitions
- Counter animations

Never overdo animations.

---

# HALAL EXPERIENCE

This is a **Halal Certified Café**.

This MUST be visible throughout the website.

Display trust indicators such as:

- Halal Certified
- 100% Alcohol-Free
- Fresh Ingredients
- Family Friendly
- Premium Specialty Coffee

The "Mojitos" section must always be presented as:

```
Alcohol-Free Mojitos (Mocktails)
```

Never use imagery or language associated with alcoholic beverages.

---

# MENU CATEGORIES

The website must support the following menu categories:

- Hot Coffee
- Iced Coffee
- Frappes
- Matcha
- Milkshakes
- Fresh Juices
- Smoothies
- Signature Drinks
- Hot Non-Coffee
- Alcohol-Free Mojitos (Mocktails)
- Breakfast
- Bakery
- Desserts
- Middle Eastern Desserts

Each category should have:

- Hero banner
- Description
- Featured products
- Filters
- Search

---

# WEBSITE FEATURES

- Beautiful Homepage
- Dynamic Menu
- Search
- Category Filters
- Gallery
- About
- Contact
- Google Maps
- WhatsApp Integration
- Testimonials
- FAQs
- Privacy Policy
- Responsive Navigation
- Sticky Navbar
- Sticky Mobile Bottom Navigation
- Floating WhatsApp Button
- Dark Mode
- SEO Optimized
- Fast Loading

---

# DJANGO REQUIREMENTS

## IMPORTANT

Every page that contains long-form content MUST use:

```
django-ckeditor-5
```

Examples include:

- About Us
- Our Story
- FAQs
- Privacy Policy
- Terms
- Blog (future)
- Homepage rich content sections
- Promotional landing pages
- Announcements
- Hero section descriptions (where editable)
- Category descriptions
- Menu item descriptions
- Gallery captions
- Testimonials
- Footer company information

Do NOT use TextField for rich editable content where CKEditor-5 is appropriate.

---

# DJANGO ADMIN

The Django Admin URL MUST be:

```
/kawas_admin/
```

Admin interface MUST use:

```
Django Unfold
```

The admin should be elegant, organized, searchable, and optimized for non-technical staff.

Use:

- fieldsets
- tabs
- list_display
- list_filter
- search_fields
- autocomplete_fields
- image previews
- ordering
- custom actions
- readonly fields where appropriate

---

# MEDIA MANAGEMENT

All products, menu items, galleries, hero banners, promotional banners, and other visual content must be manageable through Django Admin.

---

# IMAGES

Support:

- Hero Images
- Product Images
- Gallery Images
- Category Images
- Promotional Banners
- Testimonials

Automatically generate thumbnails where appropriate.

---

# DJANGO APPLICATIONS

Create the project using modular Django apps.

Recommended apps:

```
core
```

General website configuration.

---

```
accounts
```

Future authentication.

---

```
menu
```

Categories

Products

Pricing

Featured Items

Search

Filters

Availability

---

```
pages
```

# Pages (MUST ADD ALL)

- Home
- Menu - This MUST be categorised as follows{
-- Hot Coffee
-- Hot Non-Coffee
-- Iced Coffee
-- Frappes
-- Matcha
-- Milkshake
-- Fresh Juice
-- Signature Drinks
-- Smoothies
-- Mojitos
-- Desserts / Kawa's Desserts
}
- Breakfast
- Gallery
- Our Story
- Visit Us
- Contact
- FAQs
- Privacy Policy
- Terms

Rich content

---

# MENU ITEM ACTIONS (MANDATORY)

Every menu item displayed anywhere on the website (category pages, search results, featured products, related products, homepage sections, etc.) MUST include **four (4) action buttons**.

## Required Buttons

### 1. Order

Primary CTA.

This button should add the menu item to the future ordering system/cart.

For Phase 1, it may display a "Coming Soon" modal if online ordering has not yet been implemented.

---

### 2. WhatsApp Order

This button is **MANDATORY**.

It should open WhatsApp with a dynamically generated pre-filled message using Django template variables.

The message MUST include:

- Greeting with emoji
- Customer's interest
- Current Menu Item Title
- Current Menu Item Individual URL

Example:

```text
👋 Hello KAWA'S Café!

I am interested in your **{{ menu_item.title }}**.

Menu Item Link:
{{ request.build_absolute_uri }}

Thank you!
```

Example URL generation:

```django
https://wa.me/254119000999?text={{ whatsapp_message|urlencode }}
```

The WhatsApp message MUST be dynamically generated from the current menu item.

Never hardcode menu names or URLs.

This functionality must work from:

- Menu Cards
- Featured Products
- Search Results
- Related Products
- Individual Product Pages
- Wishlist (future)

---

### 3. View Details

Every menu item MUST have its own dedicated detail page.

Example URLs:

```
/menu/spanish-latte/

/menu/pistachio-latte/

/menu/kunafa-cream/
```

This page should be beautifully designed and significantly more detailed than the menu card.

It should include:

- Large Hero Image
- Multiple Gallery Images (optional)
- Product Name
- Category
- Price(s)
- Availability
- Short Description
- Full Rich Description
- Ingredients
- Allergens (optional)
- Preparation Notes
- Related Products
- Featured Badge
- Best Seller Badge
- New Arrival Badge
- Customer Reviews (future)
- Share Buttons
- Breadcrumb Navigation

The detailed description MUST use:

```
django-ckeditor-5
```

This page should feel like a premium product landing page rather than a simple menu page.

---

### 4. Wishlist

Every menu item should include a Wishlist button.

Phase 1

- Save locally (browser storage or session)

Future

- Authenticated user wishlist
- Saved favourites
- Recently viewed products
- Wishlist page
- Share wishlist

Use an outlined heart icon by default.

When added:

- Fill the heart
- Animate smoothly
- Display a success toast notification

---

# PRODUCT DETAIL PAGE EXPERIENCE

The Menu Item Detail Page should be one of the most visually impressive pages on the website.

It should include:

- Premium photography
- Elegant typography
- Rich storytelling
- Beautiful spacing
- Smooth animations
- Sticky "Order" and "WhatsApp Order" buttons on mobile
- Fully responsive layout
- SEO-optimized metadata
- Open Graph support
- Structured Data (Schema.org Product)
- Editable content via Django Admin using `django-ckeditor-5`

The goal is to create an experience similar to premium cafés in Dubai, Doha, or Istanbul, where every signature drink or dessert has its own luxurious presentation page.

```
gallery
```

Gallery images

Albums

---

```
testimonials
```

Customer reviews

Ratings

---

```
blog
```

Future articles

Announcements

---

```
location
```

Maps

Opening hours

---

```
orders
```

- Future online ordering
- 

---

```
settings
```

Global site settings

Logo

Social links

SEO

Contact information

Hero content

Footer

---

# DATABASE DESIGN

Use UUID primary keys where appropriate.

Include:

- slug
- created_at
- updated_at
- is_active
- ordering

Implement proper model relationships using:

- ForeignKey
- ManyToMany
- OneToOne

---

# SEO

Every page should support:

- Meta Title
- Meta Description
- Canonical URL
- Open Graph
- Twitter Cards
- JSON-LD Schema
- Sitemap
- Robots.txt

Editable via Django Admin where appropriate.

---

# PERFORMANCE

Optimize for:

- Lazy Loading
- Responsive Images
- WebP
- Compression
- Caching
- Minified assets

Aim for excellent Lighthouse scores.

---

# ACCESSIBILITY

Meet WCAG AA standards.

Support:

- Keyboard navigation
- Screen readers
- Proper contrast
- Alt text
- Semantic HTML

---

# CODING STANDARDS

Use:

- Django 5.x
- Python 3.13+
- PostgreSQL
- Tailwind CSS v4
- HTMX
- Alpine.js
- Django Unfold
- django-ckeditor-5
- Pillow
- django-imagekit
- WhiteNoise
- Gunicorn

Follow:

- PEP 8
- DRY
- SOLID
- Django Best Practices

---

# DEVELOPMENT RULES

- Build one Django app at a time.
- Fully complete and integrate each app before moving to the next.
- Ensure every app is production-ready, tested, and reusable.
- Keep templates modular using template inheritance and reusable partials/components.
- Avoid hardcoded content where it should be editable via Django Admin.
- Write clean, well-documented code with meaningful comments only where necessary.
- Ensure all URLs, models, views, templates, admin configurations, and static assets are properly wired before proceeding to the next app.

---

# EXPECTED WORKFLOW

The AI should proceed in this order:

1. Create and configure all required Django apps.
2. Configure shared settings, static files, media files, Tailwind CSS, HTMX, Alpine.js, Django Unfold, and django-ckeditor-5.
3. Build reusable base templates, layouts, navigation, footer, and UI components.
4. Implement models, admin, URLs, views, and templates for each app incrementally.
5. Populate the admin with sample data where appropriate.
6. Ensure the project remains fully functional after each completed step.
7. Continue until the entire KAWA'S website is complete and production-ready.

**Do not skip steps, generate placeholder code, or leave incomplete implementations. Every feature should be fully functional before proceeding to the next.**