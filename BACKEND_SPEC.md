# Backend API Specification - TechHub Pondicherry

## 🔧 Technology Stack Recommendations

### Backend Framework
- **Node.js + Express.js** (Recommended)
- **NestJS** (For larger scale)
- **Python + FastAPI** (Alternative)

### Database
- **MongoDB** (Recommended for flexibility)
- **PostgreSQL** (For relational structure)

### Additional Services
- **Redis** - Caching and sessions
- **AWS S3 / Cloudinary** - Image storage
- **SendGrid / AWS SES** - Email service
- **Twilio** - SMS notifications
- **Razorpay / PayU** - Payment gateway

## 📡 API Endpoints

### Base URL
```
Production: https://api.techhubpondy.com/v1
Development: http://localhost:3000/v1
```

---

## 🔐 Authentication

### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+919876543210",
  "password": "securePassword123"
}

Response: 201 Created
{
  "success": true,
  "data": {
    "userId": "user_123",
    "token": "jwt_token_here",
    "user": {
      "id": "user_123",
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "+919876543210"
    }
  }
}
```

### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securePassword123"
}

Response: 200 OK
{
  "success": true,
  "data": {
    "token": "jwt_token_here",
    "user": { ... }
  }
}
```

### Verify Token
```http
GET /api/auth/verify
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "data": {
    "userId": "user_123",
    "valid": true
  }
}
```

---

## 🛍️ Products

### List Products
```http
GET /api/products?page=1&limit=20&category=laptops&sort=price_asc

Query Parameters:
- page (number): Page number (default: 1)
- limit (number): Items per page (default: 20, max: 100)
- category (string): Filter by category slug
- search (string): Search query
- minPrice (number): Minimum price filter
- maxPrice (number): Maximum price filter
- brand (string): Filter by brand
- inStock (boolean): Show only in-stock items
- sort (string): price_asc, price_desc, rating_desc, newest, bestseller

Response: 200 OK
{
  "success": true,
  "data": {
    "products": [...],
    "pagination": {
      "currentPage": 1,
      "totalPages": 10,
      "totalItems": 200,
      "itemsPerPage": 20
    }
  }
}
```

### Get Product Details
```http
GET /api/products/:productId

Response: 200 OK
{
  "success": true,
  "data": {
    "id": "p1",
    "name": "Dell Latitude 7420",
    "category": "laptops",
    "price": 85000,
    "images": ["url1", "url2"],
    "description": "...",
    "specifications": {...},
    "brand": "Dell",
    "inStock": true,
    "stockCount": 8,
    "rating": 4.7,
    "reviewCount": 34,
    "reviews": [...]
  }
}
```

### Get Related Products
```http
GET /api/products/:productId/related?limit=4

Response: 200 OK
{
  "success": true,
  "data": [...]
}
```

---

## 🛒 Cart

### Get Cart
```http
GET /api/cart
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "cart_item_1",
        "product": {...},
        "quantity": 2,
        "subtotal": 170000
      }
    ],
    "total": 170000,
    "itemCount": 2
  }
}
```

### Add to Cart
```http
POST /api/cart
Authorization: Bearer {token}
Content-Type: application/json

{
  "productId": "p1",
  "quantity": 2
}

Response: 201 Created
{
  "success": true,
  "message": "Product added to cart",
  "data": {
    "cartItem": {...}
  }
}
```

### Update Cart Item
```http
PUT /api/cart/:cartItemId
Authorization: Bearer {token}
Content-Type: application/json

{
  "quantity": 3
}

Response: 200 OK
{
  "success": true,
  "message": "Cart updated",
  "data": {...}
}
```

### Remove from Cart
```http
DELETE /api/cart/:cartItemId
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "message": "Item removed from cart"
}
```

### Clear Cart
```http
DELETE /api/cart
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "message": "Cart cleared"
}
```

---

## 💝 Wishlist

### Get Wishlist
```http
GET /api/wishlist
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "data": {
    "items": [...]
  }
}
```

### Add to Wishlist
```http
POST /api/wishlist
Authorization: Bearer {token}
Content-Type: application/json

{
  "productId": "p1"
}

Response: 201 Created
```

### Remove from Wishlist
```http
DELETE /api/wishlist/:productId
Authorization: Bearer {token}

Response: 200 OK
```

---

## 📦 Orders

### Create Order
```http
POST /api/orders
Authorization: Bearer {token}
Content-Type: application/json

{
  "items": [
    {
      "productId": "p1",
      "quantity": 2,
      "price": 85000
    }
  ],
  "shippingAddress": {
    "name": "John Doe",
    "phone": "+919876543210",
    "email": "john@example.com",
    "addressLine1": "123 Street",
    "city": "Pondicherry",
    "state": "Puducherry",
    "pincode": "605001"
  },
  "paymentMethod": "cod" | "online",
  "notes": "Optional delivery notes"
}

Response: 201 Created
{
  "success": true,
  "data": {
    "orderId": "ORD_123456",
    "orderNumber": "TH202605070001",
    "total": 170000,
    "status": "pending",
    "paymentStatus": "pending",
    "estimatedDelivery": "2026-05-10"
  }
}
```

### Get Order Details
```http
GET /api/orders/:orderId
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "data": {
    "id": "ORD_123456",
    "orderNumber": "TH202605070001",
    "items": [...],
    "total": 170000,
    "status": "shipped",
    "paymentStatus": "completed",
    "shippingAddress": {...},
    "trackingNumber": "TRACK123",
    "createdAt": "2026-05-07T10:00:00Z",
    "updatedAt": "2026-05-08T14:30:00Z"
  }
}
```

### Get Order History
```http
GET /api/orders?page=1&limit=10&status=all
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "data": {
    "orders": [...],
    "pagination": {...}
  }
}
```

### Track Order
```http
GET /api/orders/:orderId/track

Response: 200 OK
{
  "success": true,
  "data": {
    "orderId": "ORD_123456",
    "status": "in_transit",
    "timeline": [
      {
        "status": "order_placed",
        "timestamp": "2026-05-07T10:00:00Z",
        "message": "Order placed successfully"
      },
      {
        "status": "processing",
        "timestamp": "2026-05-07T14:00:00Z",
        "message": "Order is being processed"
      },
      {
        "status": "shipped",
        "timestamp": "2026-05-08T09:00:00Z",
        "message": "Order shipped",
        "trackingNumber": "TRACK123"
      }
    ]
  }
}
```

---

## ⭐ Reviews

### Get Product Reviews
```http
GET /api/reviews/product/:productId?page=1&limit=10&sort=recent

Response: 200 OK
{
  "success": true,
  "data": {
    "reviews": [
      {
        "id": "rev_1",
        "userId": "user_123",
        "userName": "John Doe",
        "rating": 5,
        "comment": "Excellent product!",
        "verified": true,
        "createdAt": "2026-05-01T10:00:00Z",
        "helpful": 5
      }
    ],
    "stats": {
      "averageRating": 4.7,
      "totalReviews": 34,
      "ratingDistribution": {
        "5": 20,
        "4": 10,
        "3": 3,
        "2": 1,
        "1": 0
      }
    },
    "pagination": {...}
  }
}
```

### Add Review
```http
POST /api/reviews
Authorization: Bearer {token}
Content-Type: application/json

{
  "productId": "p1",
  "rating": 5,
  "comment": "Excellent product! Fast delivery.",
  "orderId": "ORD_123456" // Optional, for verified purchases
}

Response: 201 Created
{
  "success": true,
  "message": "Review submitted successfully",
  "data": {
    "reviewId": "rev_1"
  }
}
```

---

## 📧 Contact & Enquiries

### Submit Enquiry
```http
POST /api/enquiry
Content-Type: application/json

{
  "name": "John Doe",
  "phone": "+919876543210",
  "email": "john@example.com",
  "serviceType": "cctv_installation" | "amc" | "bulk_supply" | "networking",
  "message": "I need CCTV installation for my office",
  "preferredContactTime": "morning" | "afternoon" | "evening"
}

Response: 201 Created
{
  "success": true,
  "message": "Enquiry submitted. We'll contact you soon!",
  "data": {
    "enquiryId": "ENQ_123456",
    "estimatedResponseTime": "24 hours"
  }
}
```

### Contact Form
```http
POST /api/contact
Content-Type: application/json

{
  "name": "John Doe",
  "phone": "+919876543210",
  "email": "john@example.com",
  "subject": "Product inquiry",
  "message": "Message here"
}

Response: 201 Created
```

### Newsletter Signup
```http
POST /api/newsletter
Content-Type: application/json

{
  "email": "john@example.com",
  "name": "John Doe"
}

Response: 201 Created
{
  "success": true,
  "message": "Successfully subscribed to newsletter"
}
```

---

## 👤 User Profile

### Get Profile
```http
GET /api/user/profile
Authorization: Bearer {token}

Response: 200 OK
{
  "success": true,
  "data": {
    "id": "user_123",
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+919876543210",
    "addresses": [...],
    "createdAt": "2026-01-01T00:00:00Z"
  }
}
```

### Update Profile
```http
PUT /api/user/profile
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "John Doe Updated",
  "phone": "+919876543210"
}

Response: 200 OK
```

### Add Address
```http
POST /api/user/addresses
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "Home",
  "phone": "+919876543210",
  "addressLine1": "123 Street",
  "addressLine2": "Apartment 4B",
  "city": "Pondicherry",
  "state": "Puducherry",
  "pincode": "605001",
  "landmark": "Near temple",
  "isDefault": true
}

Response: 201 Created
```

---

## 📊 Admin APIs (Protected)

### Dashboard Stats
```http
GET /api/admin/dashboard
Authorization: Bearer {admin_token}

Response: 200 OK
{
  "success": true,
  "data": {
    "todayOrders": 15,
    "todayRevenue": 450000,
    "pendingOrders": 8,
    "lowStockProducts": 5,
    "recentOrders": [...],
    "topProducts": [...]
  }
}
```

### Manage Products
```http
POST /api/admin/products
PUT /api/admin/products/:id
DELETE /api/admin/products/:id
```

### Manage Orders
```http
GET /api/admin/orders
PUT /api/admin/orders/:id/status
```

---

## 🔔 Notifications

### Send Order Confirmation
- Email: Order details, invoice
- SMS: Order number, tracking link
- WhatsApp: Order updates (optional)

### Send Delivery Updates
- Email: Shipping confirmation
- SMS: Out for delivery notification
- WhatsApp: Delivery photo (optional)

---

## 🔒 Security Implementation

### Rate Limiting
```javascript
// 100 requests per 15 minutes per IP
app.use('/api/', rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
}));

// 5 login attempts per hour
app.use('/api/auth/login', rateLimit({
  windowMs: 60 * 60 * 1000,
  max: 5
}));
```

### Input Validation
- Use Joi or Yup for request validation
- Sanitize all user inputs
- Validate file uploads (size, type)

### Authentication
- JWT tokens with 7-day expiry
- Refresh tokens for extended sessions
- Secure password hashing (bcrypt, rounds: 12)

### CORS Configuration
```javascript
{
  origin: ['https://techhubpondy.com', 'https://www.techhubpondy.com'],
  credentials: true
}
```

---

## 📝 Error Responses

### Standard Error Format
```json
{
  "success": false,
  "error": {
    "code": "PRODUCT_NOT_FOUND",
    "message": "Product not found",
    "details": "Product with ID 'p1' does not exist"
  }
}
```

### Common Error Codes
- `UNAUTHORIZED` - 401
- `FORBIDDEN` - 403
- `NOT_FOUND` - 404
- `VALIDATION_ERROR` - 400
- `SERVER_ERROR` - 500
- `RATE_LIMIT_EXCEEDED` - 429

---

## 🧪 Testing Requirements

### Unit Tests
- Service functions
- Validation logic
- Utility functions

### Integration Tests
- API endpoints
- Database operations
- Payment gateway integration

### Load Testing
- 1000 concurrent users
- Response time < 200ms
- 99.9% uptime

---

## 📦 Deployment Checklist

- [ ] Environment variables configured
- [ ] Database indexes created
- [ ] SSL certificate installed
- [ ] Backup strategy in place
- [ ] Monitoring setup (New Relic, Datadog)
- [ ] Logging configured (Winston, Morgan)
- [ ] CDN configured for static assets
- [ ] Payment gateway in production mode
- [ ] Email/SMS service configured
- [ ] Rate limiting enabled
- [ ] CORS configured
- [ ] Health check endpoint `/api/health`

---

## 🚀 Recommended Hosting

### Backend
- **AWS EC2** or **DigitalOcean Droplet**
- **Heroku** (easy deployment)
- **Railway** (modern alternative)

### Database
- **MongoDB Atlas** (managed)
- **AWS RDS** (PostgreSQL)

### File Storage
- **AWS S3**
- **Cloudinary** (images)

---

Built for TechHub Pondicherry
