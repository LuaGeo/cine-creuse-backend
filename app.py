# Main Flask application file

from flask import Flask
from db import get_db
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
# Initialize database
get_db(app)

# Import routes
from routes.user import setup_user_routes
from routes.favorite_movies import setup_favorite_movies_routes

setup_user_routes(app)
setup_favorite_movies_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

