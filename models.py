# Data models

from db import mongo
from werkzeug.security import generate_password_hash
import uuid

def register_user(data):
    # Validate data here (ensure username, email, and password are provided)
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return {"error": "Missing information"}

    # Check if the user already exists
    if mongo.db.users.find_one({"username": data['username']}):
        return {"error": "Username already exists"}

    # Generate a unique token for the user
    token = str(uuid.uuid4())

    # Hash the password
    hashed_password = generate_password_hash(data['password'])

    # Create the user document to store in MongoDB
    user_document = {
        "username": data['username'],
        "email": data['email'],
        "password": hashed_password,
        "token": token
    }

    # Insert the user document into the database
    mongo.db.users.insert_one(user_document)
    
    return {"message": "User registered successfully", "username": data['username']}

