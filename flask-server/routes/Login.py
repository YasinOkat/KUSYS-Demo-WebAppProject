from flask import request, jsonify, Blueprint

from main import app
from models.Student import Student
from models.User import User
from forms.LoginForm import LoginForm
from utilities.utilities import generate_token
import bleach

login_bp = Blueprint('login_bp', __name__)


@app.route('/login', methods=['POST'])
def login():


    data = request.json
    username = data.get('username')
    password = data.get('password')

    username = bleach.clean(username, tags=[], attributes={}, strip=True)
    password = bleach.clean(password, tags=[], attributes={}, strip=True) 

    user = User.query.filter_by(username=username).first()

    print(username)
    print(password)

    if user and user.check_password(password.encode('utf-8')):
        token = generate_token(user.user_id, user.role)  # Generate token here
        user_id = user.user_id
        user_role = user.role
        student = Student.query.filter_by(user_id=user_id).first()  # Moved this line here
        if student:
            user_id = student.student_id
        print(user_id)
        return jsonify({'success': True, 'token': token, 'user_id': user_id,
                        'user_role': user_role})  # Include the token in the response
    return jsonify({'success': False})
