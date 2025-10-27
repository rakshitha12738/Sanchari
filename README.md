# 🌍 SANCHARI - Smart Travel Guide

A comprehensive travel guide web application for exploring India's diverse states with rich cultural information, travel tips, and hidden gems.

## Features

- **State-based Travel Information**: Detailed information about 8 major Indian states
- **Popular & Hidden Places**: Discover both famous attractions and off-the-beaten-path destinations
- **Dynamic Content**: Real-time data fetching from JSON database
- **Interactive Navigation**: Seamless navigation between main page and detailed information page
- **Search Functionality**: Quick search to find destinations
- **Responsive Design**: Modern, beautiful UI that works on all devices

## Project Structure

```
ABCD/
├── index.html          # Main landing page with state listings
├── index2.html         # Detailed information page with dynamic content
├── server.js           # Express server with API endpoints
├── travel_database.json # Comprehensive travel data for all states
├── field_project.json  # MongoDB connection configuration
├── package.json        # Node.js dependencies
└── README.md           # This file
```

## Installation

1. Navigate to the project directory:
```bash
cd ABCD
```

2. Install dependencies:
```bash
npm install
```

3. Start the server:
```bash
npm start
```

4. Open your browser and visit:
```
http://localhost:3000
```

## How It Works

### Data Flow

1. **Database**: `travel_database.json` contains comprehensive information about Indian states including:
   - Popular places
   - Hidden gems
   - Local food
   - Best time to visit
   - Safety information
   - Historical context
   - Adventure activities

2. **Server** (`server.js`):
   - Serves static files (HTML, CSS, JS)
   - Provides API endpoints for fetching travel data
   - Handles search functionality
   - Loads data from JSON database

3. **Frontend**:
   - `index.html`: Main page showing all states with scrolling sections
   - `index2.html`: Detailed page with dynamic content based on URL parameters
   - JavaScript fetches data from API endpoints
   - Both pages are interconnected with navigation links

### API Endpoints

- `GET /api/states` - Get all state information
- `GET /api/states/:name` - Get specific state details
- `POST /api/search` - Search states by name or places

### Navigation

- From `index.html`: Click state headings or use "Explore More Details" button to go to `index2.html`
- From `index2.html`: Click "🏠 Home" link in navigation bar to return to `index.html`
- State-specific content is passed via URL parameters

## Features Explained

### Index.html (Main Page)
- **Search Bar**: Enter any destination to quickly navigate to state information
- **State Suggestions**: Click state tags to auto-scroll to that section
- **State Sections**: Beautiful sections for each state with background images
- **Explore Button**: Navigate to detailed information page

### Index2.html (Details Page)
- **Dynamic Content**: Content adapts based on URL state parameter
- **Fixed Navigation Bar**: Always accessible, scrolls with page
- **Sections**: History, Food, Adventure, Safety, and Attractions
- **Home Link**: Quick return to main page

## Improvements Made

1. ✅ Created comprehensive travel database with detailed state information
2. ✅ Connected index.html and index2.html with working navigation
3. ✅ Integrated JSON database with API endpoints
4. ✅ Added JavaScript for dynamic data fetching
5. ✅ Improved user experience with smooth scrolling and interactive elements
6. ✅ Added search functionality
7. ✅ State-specific routing via URL parameters

## States Covered

1. **Kerala** - God's Own Country
2. **Tamil Nadu** - Land of Temples
3. **Karnataka** - Silicon Valley of India
4. **Assam** - Land of Tea and Rhinos
5. **Uttar Pradesh** - Heart of India
6. **Andhra Pradesh** - Rice Bowl of India
7. **Jammu and Kashmir** - Paradise on Earth
8. **Rajasthan** - Land of Kings

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Node.js, Express.js
- **Database**: JSON-based storage
- **API**: RESTful endpoints
- **Styling**: Modern CSS with gradients, animations, and responsive design

## Future Enhancements

- Add user authentication and saved preferences
- Integrate real-time weather data
- Add reviews and ratings for destinations
- Include hotel and travel booking integrations
- Add language translation support
- Expand to cover all Indian states

## Contributing

This is a student project. Feel free to suggest improvements or report issues.

## License

Educational Project - Field Project Semester 2

---

**Developed with ❤️ for exploring India's incredible diversity**
