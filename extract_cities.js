const fs = require('fs');
const path = require('path');

// Read the travel_database.json file
const dbPath = './travel_database.json';
const dbContent = fs.readFileSync(dbPath, 'utf8');
const travelData = JSON.parse(dbContent);

// Extract all cities
let allCities = [];

travelData.states.forEach(state => {
  if (state.cities) {
    Object.values(state.cities).forEach(city => {
      allCities.push(city);
    });
  }
});

// Write cities to a new JSON file
const citiesOutput = './cities.json';
fs.writeFileSync(citiesOutput, JSON.stringify(allCities, null, 2));
console.log(`Extracted ${allCities.length} cities to ${citiesOutput}`);

