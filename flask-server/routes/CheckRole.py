from flask import request, jsonify, Blueprint

from main import app
from utilities.utilities import verify_token

# Create a Blueprint named "check_role_bp"
check_role_bp = Blueprint('check_role_bp', __name__)

# The route to check the role of the logged in user
@app.route('/check_role', methods=['GET'])
def check_role():
    # Get the authorization header from the request
    authorization_header = request.headers.get('Authorization')
    
    # Checks if the header exists and starts with 'Bearer '
    if authorization_header and authorization_header.startswith('Bearer '):
        token = authorization_header.split()[1]  # Extracts the token
        payload = verify_token(token)  # Verifies the token
        
        if payload:
            role = payload.get('role')  # Gets the user's role
            return jsonify({"role": role})  # Returns the user's role
        
    return jsonify({"role": "guest"})
