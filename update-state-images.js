const { MongoClient } = require('mongodb');

const MONGO_URI = 'mongodb://localhost:27017/';
const DB_NAME = 'sanchari';

// Replace with valid Unsplash image URLs for each state
const imageUpdates = [
  { name: "Kerala", imageUrl: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80" },
  { name: "Tamil Nadu", imageUrl: "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=1600&q=80" },
  { name: "Karnataka", imageUrl: "https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?auto=format&fit=crop&w=1600&q=80" },
  { name: "Jammu and Kashmir", imageUrl: "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1600&q=80" },
  { name: "Rajasthan", imageUrl: "https://images.unsplash.com/photo-1465378552550-1caf2b7b2b36?auto=format&fit=crop&w=1600&q=80" },
  { name: "Uttar Pradesh", imageUrl: "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=1600&q=80" },
  { name: "Assam", imageUrl: "https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&w=1600&q=80" },
  { name: "Andhra Pradesh", imageUrl: "https://images.unsplash.com/photo-1519985176271-adb1088fa94c?auto=format&fit=crop&w=1600&q=80" }
];

async function updateImages() {
  const client = new MongoClient(MONGO_URI);
  try {
    await client.connect();
    const db = client.db(DB_NAME);
    const statesCollection = db.collection('states');
    for (const update of imageUpdates) {
      await statesCollection.updateOne(
        { name: update.name },
        { $set: { imageUrl: update.imageUrl } }
      );
      console.log(`Updated image for ${update.name}`);
    }
    await client.close();
    console.log('✅ All state images updated successfully.');
  } catch (err) {
    console.error('❌ Error updating images:', err);
    process.exit(1);
  }
}

updateImages();
