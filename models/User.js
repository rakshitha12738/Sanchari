const { MongoClient, ObjectId } = require('mongodb');
const bcrypt = require('bcryptjs');

const MONGO_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/';
const DB_NAME = 'travel_website';
const USERS_COLL = 'users';

class User {
    constructor(userData) {
        this.email = userData.email;
        this.password = userData.password;
        this.name = userData.name;
        this.createdAt = userData.createdAt || new Date();
        this.preferences = userData.preferences || {};
        this._id = userData._id;
    }

    static async connect() {
        if (!User.client) {
            User.client = new MongoClient(MONGO_URI);
            await User.client.connect();
            User.collection = User.client.db(DB_NAME).collection(USERS_COLL);
        }
        return User.collection;
    }

    static async findByEmail(email) {
        const collection = await User.connect();
        const userData = await collection.findOne({ email: email.toLowerCase() });
        return userData ? new User(userData) : null;
    }

    static async findById(id) {
        const collection = await User.connect();
        const userData = await collection.findOne({ _id: new ObjectId(id) });
        return userData ? new User(userData) : null;
    }

    async save() {
        const collection = await User.connect();
        
        // Hash password if it's not already hashed
        if (this.password && !this.password.startsWith('$2')) {
            this.password = await bcrypt.hash(this.password, 10);
        }

        const userData = {
            email: this.email.toLowerCase(),
            password: this.password,
            name: this.name,
            createdAt: this.createdAt,
            preferences: this.preferences
        };

        if (this._id) {
            await collection.updateOne(
                { _id: new ObjectId(this._id) },
                { $set: userData }
            );
        } else {
            const result = await collection.insertOne(userData);
            this._id = result.insertedId;
        }

        return this;
    }

    async verifyPassword(password) {
        return await bcrypt.compare(password, this.password);
    }

    toJSON() {
        return {
            id: this._id,
            email: this.email,
            name: this.name,
            preferences: this.preferences,
            createdAt: this.createdAt
        };
    }
}

module.exports = User;