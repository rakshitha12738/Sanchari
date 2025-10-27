const fs = require('fs');
const path = require('path');
const express = require('express');
const cors = require('cors');
const { MongoClient, ObjectId } = require('mongodb');
require('dotenv').config();

const appRoot = __dirname;
const dbPath = path.join(appRoot, 'travel_database.json');

// MongoDB connection configuration
const getConnString = () => {
  try {
    const fpPath = path.join(appRoot, 'field_project.json');
    const fp = JSON.parse(fs.readFileSync(fpPath, 'utf8'));
    return fp?.connections?.[0]?.connectionOptions?.connectionString || 'mongodb://localhost:27017/';
  } catch (err) {
    return 'mongodb://localhost:27017/';
  }
};

const MONGO_URI = getConnString();
const DB_NAME = 'sanchari';
const STATES_COLL = 'states';
const CITIES_COLL = 'cities';

// MongoDB client
let dbClient = null;
let db = null;
let statesColl = null;
let citiesColl = null;
let mongodbConnected = false;

// Initialize MongoDB connection with timeout
async function connectMongoDB() {
  try {
    // Create a promise with timeout
    const connectPromise = new Promise(async (resolve, reject) => {
      try {
        dbClient = new MongoClient(MONGO_URI, {
          serverSelectionTimeoutMS: 5000, // 5 second timeout
          socketTimeoutMS: 5000
        });
        
        await dbClient.connect();
        console.log('✅ Connected to MongoDB:', MONGO_URI);
        
        db = dbClient.db(DB_NAME);
        statesColl = db.collection(STATES_COLL);
        citiesColl = db.collection(CITIES_COLL);
        mongodbConnected = true;
        
        // Verify we have data
        const stateCount = await statesColl.countDocuments();
        const cityCount = await citiesColl.countDocuments();
        console.log(`📊 Database loaded: ${stateCount} states, ${cityCount} cities`);
        
        resolve(true);
      } catch (err) {
        reject(err);
      }
    });
    
    // Add timeout
    const timeoutPromise = new Promise((_, reject) => 
      setTimeout(() => reject(new Error('Connection timeout')), 5000)
    );
    
    await Promise.race([connectPromise, timeoutPromise]);
    return true;
  } catch (err) {
    console.error('❌ MongoDB connection failed:', err.message);
    console.log('⚠️  Trying to initialize with JSON file data...');
    mongodbConnected = false;
    return false;
  }
}

// Load fallback JSON data
let travelData = { states: [] };
try {
  const dbContent = fs.readFileSync(dbPath, 'utf8');
  travelData = JSON.parse(dbContent);
} catch (err) {
  console.error('Could not read travel_database.json:', err.message);
}

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(appRoot));

// Import and use authentication routes
const authRoutes = require('./routes/auth');
app.use('/api/auth', authRoutes);

// Handle favicon.ico request
app.get('/favicon.ico', (req, res) => {
  res.status(204).send(); // No content
});

// API Routes - STRICT MONGODB ONLY
app.get('/api/states', async (req, res) => {
  try {
    const states = await statesColl.find({}).toArray();
    res.json(states);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch states from MongoDB', details: error.message });
  }
});

app.get('/api/states/:name', async (req, res) => {
  try {
    const stateName = req.params.name.replace(/_/g, ' ');
    const state = await statesColl.findOne({ name: { $regex: new RegExp(stateName, 'i') } });
    if (state) {
      res.json(state);
    } else {
      res.status(404).json({ error: 'State not found in database' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch state from MongoDB', details: error.message });
  }
});

// Get city-specific information from MongoDB
app.get('/api/city/:city', async (req, res) => {
  try {
    const cityName = decodeURIComponent(req.params.city.replace(/_/g, ' '));
    
    // Try multiple search patterns
    let city = null;
    
    // 1. Try exact match
    city = await citiesColl.findOne({ name: cityName });
    
    // 2. Try case-insensitive exact match
    if (!city) {
      city = await citiesColl.findOne({ name: { $regex: new RegExp(`^${cityName}$`, 'i') } });
    }
    
    // 3. Try partial match (for cities with parentheses like "Kochi (Cochin)")
    if (!city) {
      city = await citiesColl.findOne({ name: { $regex: new RegExp(`^${cityName}`, 'i') } });
    }
    
    // 4. Try name without parentheses
    if (!city && cityName.includes('(')) {
      const nameWithoutParen = cityName.split('(')[0].trim();
      city = await citiesColl.findOne({ name: { $regex: new RegExp(`^${nameWithoutParen}`, 'i') } });
    }
    
    if (city) {
      console.log(`✅ Found city: ${city.name} for query: ${cityName}`);
      res.json(city);
    } else {
      console.log(`❌ City not found: ${cityName}`);
      res.status(404).json({ error: `City "${cityName}" not found in database` });
    }
  } catch (error) {
    console.error('Error fetching city:', error);
    res.status(500).json({ error: 'Failed to fetch city from MongoDB', details: error.message });
  }
});

// Dynamic search endpoint using MongoDB
app.post('/api/search', async (req, res) => {
  try {
    const query = req.body.query?.toLowerCase() || '';
    const results = await statesColl.find({
      $or: [
        { name: { $regex: query, $options: 'i' } },
        { popularPlaces: { $in: [new RegExp(query, 'i')] } },
        { hiddenPlaces: { $in: [new RegExp(query, 'i')] } }
      ]
    }).toArray();
    res.json(results);
  } catch (error) {
    res.status(500).json({ error: 'Search failed in MongoDB', details: error.message });
  }
});

// Gemini API chatbot endpoint
app.post('/api/chat', async (req, res) => {
  try {
    const { message } = req.body;
    
    if (!message) {
      return res.status(400).json({ response: 'Please provide a message.' });
    }

    // Get API key from environment variables
    const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
    if (!GEMINI_API_KEY) {
      throw new Error('GEMINI_API_KEY not found in environment variables');
    }
    // Use the stable Gemini 2.5 model with v1 API
    const GEMINI_API_URL = `https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=${GEMINI_API_KEY}`;
    
    const prompt = `You are a knowledgeable and friendly AI assistant for SANCHARI. 
You can answer questions about:
- Travel destinations, attractions, and activities (especially India)
- Local food, cuisine, and restaurants
- Culture, traditions, and customs
- Weather, best time to visit, and travel tips
- General knowledge and helpful information
- Safety, accommodation, and transportation

Provide helpful, accurate, and conversational responses. Keep answers concise but informative (2-4 sentences).
If you're not sure about something, be honest and suggest where they might find more information.

User question: ${message}`;

    const response = await fetch(GEMINI_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        contents: [{
          parts: [{
            text: prompt
          }]
        }],
        safetySettings: [{
          category: "HARM_CATEGORY_HARASSMENT",
          threshold: "BLOCK_MEDIUM_AND_ABOVE"
        }],
        generationConfig: {
          temperature: 0.7,
          maxOutputTokens: 200,
          topP: 0.8,
          topK: 40
        }
      }),
      timeout: 10000 // 10 second timeout
    }).catch(error => {
      console.error('Fetch error:', error);
      throw new Error('Network request failed');
    });

    // First check if we got a response
    if (!response.ok) {
      let errorMessage = `HTTP error! status: ${response.status}`;
      try {
        const errorData = await response.text(); // Get raw response text
        console.error('Raw API Error Response:', errorData);
        
        // Try to parse it as JSON if possible
        try {
          const jsonError = JSON.parse(errorData);
          console.error('Parsed API Error:', jsonError);
          errorMessage = jsonError.error?.message || errorMessage;
        } catch (parseError) {
          console.error('Could not parse error response as JSON');
        }
      } catch (error) {
        console.error('Could not read error response:', error);
      }
      throw new Error(errorMessage);
    }

    // Try to get the response data
    let responseText;
    try {
      const rawResponse = await response.text(); // Get raw response text
      console.log('Raw API Response:', rawResponse);
      
      // Try to parse as JSON
      const data = JSON.parse(rawResponse);
      responseText = data.candidates?.[0]?.content?.parts?.[0]?.text ||
                    data.text || // Try alternate response format
                    "Sorry, I couldn't process that. Please try again!";
    } catch (error) {
      console.error('Error parsing API response:', error);
      throw new Error('Failed to parse API response');
    }
    
    res.json({ response: responseText });
  } catch (error) {
    console.error('Chat API Error:', error);
    
    try {
      // Get the user's message from the request body
      const userMessage = req.body.message.toLowerCase();
      let fallbackResponse = "Sorry, I'm having trouble connecting to the AI service right now. ";
      
      if (userMessage.includes('kerala')) {
        fallbackResponse += "Kerala is known as 'God's Own Country' with beautiful backwaters, hill stations, and spice plantations. Visit our Kerala section for detailed information!";
      } else if (userMessage.includes('tamil nadu')) {
        fallbackResponse += "Tamil Nadu is the 'Land of Temples' with rich culture, beautiful beaches, and hill stations like Ooty. Check our Tamil Nadu section!";
      } else if (userMessage.includes('karnataka')) {
        fallbackResponse += "Karnataka is India's Silicon Valley with beautiful cities like Bangalore, Mysore, and Coorg. Explore our Karnataka section!";
      } else if (userMessage.includes('rajasthan')) {
        fallbackResponse += "Rajasthan is the 'Land of Kings' with magnificent palaces, deserts, and rich heritage. Visit our Rajasthan section!";
      } else if (userMessage.includes('food') || userMessage.includes('cuisine')) {
        fallbackResponse += "India offers diverse cuisines from spicy South Indian to rich Mughlai food. Each state has unique specialties!";
      } else if (userMessage.includes('weather') || userMessage.includes('climate')) {
        fallbackResponse += "India has varied climates. Hill stations are cool, coastal areas are humid, and northern plains have extreme seasons. Check specific destinations for weather info!";
      } else {
        fallbackResponse += "Please explore our destination pages for comprehensive travel information about Indian states and cities!";
      }
      
      res.json({ response: fallbackResponse });
    } catch (fallbackError) {
      // If even the fallback fails, send a generic response
      res.json({ 
        response: "Sorry, I'm having trouble processing your request. Please try exploring our destination pages for travel information!" 
      });
    }
  }
});

const port = process.env.PORT || 3000;

async function startServer() {
  // Try to connect to MongoDB
  const connected = await connectMongoDB();
  
  if (!connected) {
    console.log('\n❌ MONGODB IS REQUIRED FOR THIS APPLICATION');
    console.log('\n📝 To fix this:');
    console.log('   1. Install MongoDB Community Edition');
    console.log('   2. Start MongoDB service: net start MongoDB');
    console.log('   3. Import data: node import-to-mongodb.js');
    console.log('   4. Restart server: npm start');
    console.log('\nSee STRICT_MONGODB_SETUP.md for detailed instructions\n');
    process.exit(1);
  }
  
  app.listen(port, () => {
    console.log(`\n====================================`);
    console.log(`🌍 SANCHARI - Travel Guide Server`);
    console.log(`====================================`);
    console.log(`Server running at http://localhost:${port}`);
    console.log(`✅ Database: MongoDB (${MONGO_URI})`);
    console.log(`📊 Database loaded: 8 states, 17 cities`);
    console.log(`\nPages available:`);
    console.log(`  - Main page: http://localhost:${port}/index.html`);
    console.log(`  - Details page: http://localhost:${port}/index2.html`);
    console.log(`\nAPI Endpoints:`);
    console.log(`  - GET /api/states - Get all states from MongoDB`);
    console.log(`  - GET /api/states/:name - Get specific state from MongoDB`);
    console.log(`  - GET /api/city/:city - Get city details from MongoDB`);
    console.log(`  - POST /api/search - Search states in MongoDB`);
    console.log(`====================================\n`);
  });
}

startServer().catch(err => {
  console.error('❌ Server start failed:', err);
  process.exit(1);
});

// Graceful shutdown
process.on('SIGINT', async () => {
  console.log('\n\nShutting down gracefully...');
  if (dbClient) {
    await dbClient.close();
    console.log('MongoDB connection closed.');
  }
  process.exit(0);
});