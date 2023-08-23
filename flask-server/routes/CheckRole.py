from flask import request, jsonify, Blueprint

from main import app
from utilities.utilities import verify_token

check_role_bp = Blueprint('check_role_bp', __name__)

@app.route('/check_role', methods=['GET'])
def check_role():
    authorization_header = request.headers.get('Authorization')
    
    if authorization_header and authorization_header.startswith('Bearer '):
        token = authorization_header.split()[1]  # Extract the token
        payload = verify_token(token)
        if payload:
            role = payload.get('role')  # Get the user's role from the payload
            return jsonify({"role": role})  # Return the user's role
    # If no valid token or header, return default guest role
    return jsonify({"role": "guest"})