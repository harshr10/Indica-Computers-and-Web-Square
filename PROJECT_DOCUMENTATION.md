# TechHub Pondicherry - IT Solutions Ecommerce Website

## 🚀 Project Overview

A modern, premium, fully responsive ecommerce and business website for a 25-year-old IT hardware and technology solutions company based in Pondicherry, India.

### Tech Stack

- **Frontend**: React 18.3 + TypeScript
- **Styling**: Tailwind CSS v4
- **Animations**: Framer Motion (Motion)
- **Icons**: Lucide React
- **UI Components**: Radix UI primitives
- **Build Tool**: Vite
- **State Management**: React Context API
- **Notifications**: Sonner (Toast)

## 📁 Project Structure

```
src/
├── app/
│   ├── components/
│   │   ├── home/              # Homepage sections
│   │   │   ├── HeroSection.tsx
│   │   │   ├── FeaturedCategories.tsx
│   │   │   ├── BestSellers.tsx
│   │   │   ├── BrandsSection.tsx
│   │   │   ├── ServicesPreview.tsx
│   │   │   ├── CorporateSection.tsx
│   │   │   ├── TestimonialsSection.tsx
│   │   │   ├── BlogPreview.tsx
│   │   │   ├── WhyChooseUs.tsx
│   │   │   └── ContactSection.tsx
│   │   ├── cart/              # Cart components
│   │   │   └── CartDrawer.tsx
│   │   ├── services/          # Service pages
│   │   │   └── ServiceDetailPage.tsx
│   │   ├── ui/                # Reusable UI components (Radix)
│   │   ├── Header.tsx         # Main navigation header
│   │   ├── Footer.tsx         # Site footer
│   │   ├── ProductCard.tsx    # Product display card
│   │   ├── WhatsAppButton.tsx # WhatsApp integration
│   │   └── SEOHead.tsx        # SEO utilities
│   ├── context/
│   │   ├── CartContext.tsx    # Shopping cart state
│   │   └── WishlistContext.tsx # Wishlist state
│   ├── data/
│   │   └── mockData.ts        # Sample data
│   ├── types/
│   │   └── index.ts           # TypeScript types
│   └── App.tsx                # Main app component
├── styles/
│   ├── index.css
│   ├── tailwind.css
│   ├── theme.css
│   └── fonts.css
└── package.json
```

## 🎨 Features Implemented

### 1. Homepage
- ✅ Hero banner with carousel
- ✅ Featured product categories
- ✅ Best sellers section
- ✅ Why choose us section
- ✅ Brand partners showcase
- ✅ Professional services preview
- ✅ Corporate/B2B solutions section
- ✅ Customer testimonials
- ✅ Google reviews integration
- ✅ Blog preview section
- ✅ Contact section with Google Maps
- ✅ Newsletter signup

### 2. Ecommerce Features
- ✅ Product cards with images, pricing, ratings
- ✅ Shopping cart with context API
- ✅ Wishlist functionality
- ✅ Add to cart with toast notifications
- ✅ Cart drawer with quantity controls
- ✅ Stock indicators
- ✅ Discount badges
- ✅ Bestseller and new arrival tags

### 3. Product Categories
- ✅ Laptops (Gaming, Business)
- ✅ Desktops & Custom PCs
- ✅ Printers (Laser, Inkjet, Multifunction)
- ✅ CCTV Systems (IP, DVR, NVR)
- ✅ Networking (Routers, Switches)
- ✅ Gaming Accessories
- ✅ Monitors
- ✅ Storage Devices

### 4. Services
- ✅ CCTV Installation
- ✅ Computer AMC Services
- ✅ Office Networking Solutions
- ✅ Bulk Laptop Supply
- ✅ Service detail page template
- ✅ FAQ sections
- ✅ Benefits highlighting
- ✅ Target customer showcase

### 5. WhatsApp Integration
- ✅ Floating WhatsApp button (bottom right)
- ✅ Product enquiry buttons
- ✅ Service inquiry CTAs
- ✅ Customizable pre-filled messages

### 6. Corporate/B2B Section
- ✅ Enterprise solutions showcase
- ✅ Target industries (Schools, Offices, Hotels, Hospitals)
- ✅ AMC contracts information
- ✅ Bulk order information
- ✅ Statistics and trust indicators

### 7. Trust Elements
- ✅ 25+ years experience badge
- ✅ Customer statistics
- ✅ Google reviews rating
- ✅ Contact information (phone, email, address)
- ✅ Working hours
- ✅ Google Maps integration
- ✅ Social media links
- ✅ Trust badges (warranty, support, delivery)

### 8. UI/UX
- ✅ Premium, modern design
- ✅ Smooth Framer Motion animations
- ✅ Sticky navigation header
- ✅ Mobile-responsive design
- ✅ Professional color scheme
- ✅ Soft shadows and rounded cards
- ✅ Hover effects and transitions
- ✅ Loading states
- ✅ Toast notifications

### 9. SEO Optimization
- ✅ SEO meta data templates
- ✅ Schema.org markup for local business
- ✅ Optimized page structure
- ✅ Semantic HTML
- ✅ Keyword-rich content
- ✅ Alt tags for images

## 🛠️ Setup Instructions

### Prerequisites
- Node.js 18+ 
- pnpm (recommended) or npm

### Installation

```bash
# Install dependencies
pnpm install

# Start development server (already running in Figma Make)
# The dev server is automatically running
```

### Environment Variables

Create a `.env` file in the root directory:

```env
# Company Information
VITE_COMPANY_NAME=TechHub Pondicherry
VITE_COMPANY_PHONE=+919876543210
VITE_COMPANY_WHATSAPP=+919876543210
VITE_COMPANY_EMAIL=info@techhubpondy.com

# API Endpoints (when backend is ready)
VITE_API_URL=http://localhost:3000/api
VITE_PAYMENT_GATEWAY_KEY=your_key_here
```

## 🔧 Customization Guide

### Update Company Information

Edit `/src/app/data/mockData.ts`:

```typescript
export const companyInfo = {
  name: 'Your Company Name',
  phone: '+91XXXXXXXXXX',
  whatsapp: '+91XXXXXXXXXX',
  email: 'your@email.com',
  address: 'Your Address',
  // ... more fields
};
```

### Add Products

Add to the `products` array in `/src/app/data/mockData.ts`:

```typescript
{
  id: 'unique-id',
  name: 'Product Name',
  category: 'Category',
  price: 50000,
  image: 'image-url',
  // ... more fields
}
```

### Modify Colors

Edit `/src/styles/theme.css` for global theme colors:

```css
:root {
  --color-primary: #2563eb; /* Blue-600 */
  --color-secondary: #10b981; /* Green-500 */
  /* ... more colors */
}
```

## 📱 Mobile Responsiveness

The website is fully responsive with breakpoints:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## 🚀 Deployment

### Build for Production

```bash
# Build the project
pnpm build

# Preview production build
pnpm preview
```

### Deployment Platforms

#### Vercel (Recommended)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

#### Netlify
```bash
# Build command
pnpm build

# Publish directory
dist
```

#### Traditional Hosting
1. Run `pnpm build`
2. Upload `dist` folder to your web server
3. Configure server to serve `index.html` for all routes

## 🔌 Backend Integration

### API Endpoints Needed

```typescript
// Products
GET    /api/products              // List products
GET    /api/products/:id          // Get product details
GET    /api/products/category/:cat // Products by category
GET    /api/products/search?q=    // Search products

// Cart & Orders
POST   /api/cart                  // Add to cart
GET    /api/cart                  // Get cart
PUT    /api/cart/:id              // Update cart item
DELETE /api/cart/:id              // Remove from cart
POST   /api/orders                // Create order
GET    /api/orders/:id            // Get order details

// User
POST   /api/auth/register         // Register user
POST   /api/auth/login            // Login
GET    /api/user/profile          // Get profile
PUT    /api/user/profile          // Update profile
GET    /api/user/orders           // Order history

// Services
POST   /api/enquiry               // Service enquiry
POST   /api/contact               // Contact form
POST   /api/newsletter            // Newsletter signup

// Reviews
GET    /api/reviews/:productId    // Get reviews
POST   /api/reviews               // Add review
```

### Database Schema (MongoDB)

```javascript
// Products Collection
{
  _id: ObjectId,
  name: String,
  category: String,
  price: Number,
  images: [String],
  description: String,
  specifications: Object,
  brand: String,
  inStock: Boolean,
  stockCount: Number,
  createdAt: Date,
  updatedAt: Date
}

// Orders Collection
{
  _id: ObjectId,
  userId: ObjectId,
  items: [{
    productId: ObjectId,
    quantity: Number,
    price: Number
  }],
  total: Number,
  status: String,
  paymentMethod: String,
  shippingAddress: Object,
  createdAt: Date
}

// Users Collection
{
  _id: ObjectId,
  name: String,
  email: String,
  phone: String,
  password: String (hashed),
  addresses: [Object],
  wishlist: [ObjectId],
  createdAt: Date
}
```

## 🔒 Security Considerations

1. **API Keys**: Never commit API keys to repository
2. **Input Validation**: Validate all form inputs
3. **XSS Protection**: Sanitize user-generated content
4. **HTTPS**: Always use HTTPS in production
5. **Payment Gateway**: Use PCI-compliant payment processors
6. **Rate Limiting**: Implement rate limiting on API endpoints

## 📈 Performance Optimization

- ✅ Image lazy loading
- ✅ Component code splitting (ready for implementation)
- ✅ Minimal bundle size
- ✅ Efficient re-renders with React.memo (where needed)
- ✅ Optimized animations with Framer Motion
- ⚠️ Consider implementing:
  - Image optimization (WebP format)
  - CDN for static assets
  - Service worker for caching
  - Lighthouse score optimization

## 🎯 Next Steps / Future Enhancements

1. **User Authentication**
   - Login/Register system
   - User dashboard
   - Order tracking

2. **Payment Integration**
   - Razorpay / PayU integration
   - COD confirmation system
   - Invoice generation

3. **Admin Dashboard**
   - Product management
   - Order management
   - Analytics dashboard
   - Inventory tracking

4. **Additional Features**
   - Product comparison
   - Advanced filters
   - Live chat support
   - Email notifications
   - SMS notifications
   - Loyalty program
   - Referral system

5. **SEO & Marketing**
   - Google Analytics integration
   - Facebook Pixel
   - Sitemap generation
   - Blog system implementation
   - Email marketing integration

## 📞 Support

For questions or support, contact:
- Email: info@techhubpondy.com
- Phone: +91 9876543210
- WhatsApp: +91 9876543210

---

Built with ❤️ for TechHub Pondicherry
