# SANCHARI Authentication Flow

## Overview
SANCHARI now has a complete authentication system with a beautiful, modern login page.

## Features

### 1. **Dedicated Login Page** (`login.html`)
- Beautiful split-screen design
- Login and registration forms
- Password visibility toggle
- Form validation
- Success/error alerts
- Smooth animations
- Fully responsive

### 2. **Protected Routes**
- `index.html` and `index2.html` are now protected
- Users must login first to access the main application
- Automatic redirect to login page if not authenticated

### 3. **User Session Management**
- JWT token-based authentication
- Secure cookies with 7-day expiration
- User info stored in cookies
- Automatic session validation

### 4. **User Interface**
- User name displayed in navbar after login
- Dropdown user menu
- Logout functionality
- Seamless experience across pages

## How It Works

### First Time Access:
1. User visits `index.html` or `index2.html`
2. System checks for authentication token
3. If no token found → Redirect to `login.html`
4. User logs in or registers
5. On success → Redirect to main page

### Authenticated Access:
1. User's token is validated automatically
2. User name appears in navbar
3. User can navigate between pages freely
4. Click on name to see logout option

### Logout:
1. Click on user name in navbar
2. Select "Logout" from dropdown
3. All session data cleared
4. Redirect to login page

## API Endpoints

### Authentication Routes (`/api/auth/`)
- `POST /register` - Create new account
- `POST /login` - User login
- `GET /profile` - Get user profile (protected)
- `PUT /change-password` - Change password (protected)

### Data Routes
- `GET /api/states` - Get all states
- `GET /api/city/:name` - Get city details
- `POST /api/chat` - Chatbot interaction

## Files Structure

```
/
├── login.html              # Beautiful authentication page
├── index.html              # Main page (protected)
├── index2.html             # Details page (protected)
├── models/
│   └── User.js            # User data model
├── middleware/
│   └── auth.js            # JWT authentication middleware
├── routes/
│   └── auth.js            # Authentication routes
└── server.js              # Express server
```

## Security Features

1. **Password Hashing**: bcryptjs with salt rounds
2. **JWT Tokens**: Secure, time-limited tokens
3. **HTTP-Only Cookies**: XSS protection
4. **Input Validation**: Server-side validation
5. **Error Handling**: Secure error messages

## Testing

### Register New User:
1. Open `http://localhost:3000/login.html`
2. Click "Create Account"
3. Enter name, email, password
4. Submit form
5. Automatically logged in and redirected

### Login Existing User:
1. Open `http://localhost:3000/login.html`
2. Enter email and password
3. Optionally check "Remember me"
4. Submit form
5. Redirected to main page

### Access Protected Pages:
- Try visiting `http://localhost:3000/` or `http://localhost:3000/index.html`
- If not logged in → Automatic redirect to login
- If logged in → Page loads normally

## Environment Variables

Required in `.env` file:
```
JWT_SECRET=your_secret_key_here
```

Generate a secure secret:
```javascript
require('crypto').randomBytes(64).toString('hex')
```

## Customization

### Colors & Styling
The login page uses the same color scheme as the main site:
- Primary: #6366F1 (Indigo)
- Accent: #EC4899 (Pink)
- Secondary: #F59E0B (Amber)

### Token Expiration
Default: 7 days
Change in `routes/auth.js`:
```javascript
Cookies.set('token', data.token, { expires: 7 }); // Change 7 to desired days
```

## Troubleshooting

### Cannot Access Main Pages
- Check if server is running
- Clear cookies and try again
- Check browser console for errors

### Login Not Working
- Verify MongoDB is running
- Check `.env` file has JWT_SECRET
- Check server console for errors

### Token Issues
- Clear all cookies
- Re-login
- Check token expiration settings

## Next Steps

Possible enhancements:
1. Email verification
2. Password reset functionality
3. Social login (Google, Facebook)
4. Two-factor authentication
5. User profile management
6. Remember device feature
7. Activity logging
