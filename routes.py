# Flask routes

from app import app
from flask import request, jsonify
from models import register_user

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    response = register_user(data)
    return jsonify(response)



