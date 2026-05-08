# TechHub Pondicherry - Premium IT Solutions Website

A modern, fully responsive ecommerce and business website for an IT hardware and technology solutions company in Pondicherry, India.

## 🌟 Features

- **Ecommerce Platform**: Complete online shopping experience with cart, wishlist, and product catalog
- **Service Showcase**: Dedicated sections for IT services (CCTV, AMC, Networking, Bulk Supply)
- **Corporate Solutions**: B2B section targeting schools, offices, hospitals, and enterprises
- **WhatsApp Integration**: Floating button and contextual CTAs throughout the site
- **Premium UI/UX**: Modern design with smooth animations using Framer Motion
- **Fully Responsive**: Optimized for mobile, tablet, and desktop
- **SEO Ready**: Structured data, meta tags, and semantic HTML

## 🚀 Quick Start

```bash
# The development server is already running in Figma Make
# Just start editing files and see changes in real-time
```

## 📦 Tech Stack

- React 18 + TypeScript
- Tailwind CSS v4
- Framer Motion
- Radix UI Components
- Lucide React Icons
- Vite Build Tool

## 📖 Documentation

See [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md) for:
- Complete feature list
- Project structure
- Setup instructions
- Customization guide
- Deployment guide
- Backend integration specs
- Database schema

## 🎯 Key Sections

### Homepage
- Hero carousel with offers
- Featured product categories
- Best sellers showcase
- Why choose us
- Brand partners
- Services preview
- Corporate solutions
- Customer testimonials
- Blog preview
- Contact section

### Products
- 8 main categories (Laptops, CCTV, Printers, etc.)
- Product cards with ratings, pricing, stock status
- Cart and wishlist functionality
- Discount badges and tags

### Services
- CCTV Installation
- Computer AMC
- Networking Solutions
- Bulk Laptop Supply
- Service detail pages with FAQs

### Corporate/B2B
- Enterprise solutions
- Target industries showcase
- Statistics and trust indicators
- Dedicated inquiry system

## 🔧 Customization

### Update Company Info

Edit `src/app/data/mockData.ts`:

```typescript
export const companyInfo = {
  name: 'Your Company',
  phone: '+91XXXXXXXXXX',
  whatsapp: '+91XXXXXXXXXX',
  email: 'your@email.com',
  address: 'Your address'
};
```

### Add Products

```typescript
export const products: Product[] = [
  {
    id: 'p1',
    name: 'Product Name',
    price: 50000,
    image: 'image-url',
    // ... more fields
  }
];
```

## 📱 WhatsApp Integration

WhatsApp button appears:
- Floating on all pages (bottom-right)
- On service inquiry CTAs
- In corporate solutions section
- All buttons include pre-filled contextual messages

## 🎨 Design

- Modern, premium aesthetic
- Professional color scheme (Blue primary, Green accents)
- Smooth animations and transitions
- Responsive grid layouts
- Accessible UI components

## 🔐 Security Notes

- Sanitize all user inputs
- Use environment variables for sensitive data
- Implement HTTPS in production
- Follow PCI compliance for payments

## 📈 Next Steps

1. Connect to backend API
2. Implement user authentication
3. Integrate payment gateway (Razorpay/PayU)
4. Add admin dashboard
5. Set up analytics (Google Analytics)
6. Deploy to production

## 📞 Support

- Email: info@techhubpondy.com
- Phone: +91 9876543210
- WhatsApp: +91 9876543210

---

Built with ❤️ for TechHub Pondicherry
