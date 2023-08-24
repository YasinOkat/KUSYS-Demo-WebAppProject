from flask import jsonify, Blueprint
from flask_login import logout_user
from main import app

logout_bp = Blueprint('logout_bp', __name__)

# The logout route
@app.route('/logout')
def logout_page():
    logout_user()
    response = jsonify({'message': 'Logged out successfully'})
    return response
