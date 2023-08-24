import datetime
import os
import jwt

# Function that generates a JWT token based on user_id and role
def generate_token(user_id, role):
    jwt_secret_key = os.environ.get('JWT_SECRET_KEY')  # Get the JWT secret key from .env
    # Define payload containing user information and expiration time
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)
    }
    # Encode payload using JWT secret key and HS256 algorithm
    return jwt.encode(payload, jwt_secret_key, algorithm='HS256')

# Function to verify a JWT token
def verify_token(token):
    jwt_secret_key = os.environ.get('JWT_SECRET_KEY')  # Get JWT secret key from environment
    try:
        # Decode token using JWT secret key and HS256 algorithm
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.DecodeError:
        return None

