const { MongoClient } = require('mongodb');
const fs = require('fs');
const path = require('path');

// MongoDB configuration
const MONGO_URI = 'mongodb://localhost:27017/';
const DB_NAME = 'sanchari';
const STATES_COLL = 'states';
const CITIES_COLL = 'cities';

async function importData() {
  let client;
  
  try {
    console.log('🔌 Connecting to MongoDB...');
    client = new MongoClient(MONGO_URI);
    await client.connect();
    console.log('✅ Connected to MongoDB!');
    
    const db = client.db(DB_NAME);
    const statesColl = db.collection(STATES_COLL);
    const citiesColl = db.collection(CITIES_COLL);
    
    // Read JSON files
    const statesPath = path.join(__dirname, 'states.json');
    const citiesPath = path.join(__dirname, 'cities.json');
    
    if (!fs.existsSync(statesPath)) {
      console.error('❌ states.json not found!');
      return;
    }
    
    if (!fs.existsSync(citiesPath)) {
      console.error('❌ cities.json not found!');
      return;
    }
    
    const statesData = JSON.parse(fs.readFileSync(statesPath, 'utf8'));
    const citiesData = JSON.parse(fs.readFileSync(citiesPath, 'utf8'));
    
    console.log(`\n📥 Importing ${statesData.length} states...`);
    await statesColl.deleteMany({});
    await statesColl.insertMany(statesData);
    console.log(`✅ Imported ${statesData.length} states`);
    
    console.log(`\n📥 Importing ${citiesData.length} cities...`);
    await citiesColl.deleteMany({});
    await citiesColl.insertMany(citiesData);
    console.log(`✅ Imported ${citiesData.length} cities`);
    
    // Verify
    const stateCount = await statesColl.countDocuments();
    const cityCount = await citiesColl.countDocuments();
    
    console.log('\n====================================');
    console.log('✅ Import Complete!');
    console.log(`   States: ${stateCount}`);
    console.log(`   Cities: ${cityCount}`);
    console.log('====================================\n');
    
  } catch (error) {
    if (error.code === 'ECONNREFUSED') {
      console.error('\n❌ MongoDB Connection Failed!');
      console.error('   MongoDB is not running on localhost:27017');
      console.error('\n📝 To fix this:');
      console.error('   1. Install MongoDB Community Edition');
      console.error('   2. Start MongoDB service');
      console.error('   3. Run this script again\n');
      console.error('   Alternative: The server will work in fallback mode using JSON files.');
    } else {
      console.error('❌ Error:', error.message);
    }
  } finally {
    if (client) {
      await client.close();
      console.log('Disconnected from MongoDB');
    }
  }
}

importData();

