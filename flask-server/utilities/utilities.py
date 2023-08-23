import datetime
import os
import jwt




def generate_token(user_id, role):
    jwt_secret_key = os.environ.get('JWT_SECRET_KEY')
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5)  # Expiry time
    }
    return jwt.encode(payload, jwt_secret_key, algorithm='HS256')


def verify_token(token):
    jwt_secret_key = os.environ.get('JWT_SECRET_KEY')
    try:
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.DecodeError:
        return None  # Invalid token
