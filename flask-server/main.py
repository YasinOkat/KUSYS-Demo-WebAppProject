from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from utilities.utilities import verify_token


app = Flask(__name__)
app.debug = True
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/postgres'
app.config['SECRET_KEY'] = 'bd78312ee31cbd0b51586a57'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from models.User import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.request_loader
def load_user_from_request(request):
    token = request.headers.get('Authorization')
    if token and token.startswith('Bearer '):
        token = token.split()[1]  # Extract the token without 'Bearer'

        payload = verify_token(token)  # Implement the verify_token function
        if payload and 'user_id' in payload:
            user_id = payload['user_id']
            user = User.query.get(user_id)  # Get the user using user_id
            return user

    return None


from routes.Login import login_bp
from routes.CheckRole import check_role_bp
from routes.Courses import courses_bp
from routes.CreateStudent import create_student_bp
from routes.DeleteStudent import delete_student_bp
from routes.Logout import logout_bp
from routes.SelectCourses import select_courses_bp
from routes.StudentDetails import student_details_bp
from routes.Students import students_bp
from routes.UpdateStudent import update_student_bp

app.register_blueprint(login_bp)
app.register_blueprint(check_role_bp)
app.register_blueprint(courses_bp)
app.register_blueprint(create_student_bp)
app.register_blueprint(delete_student_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(select_courses_bp)
app.register_blueprint(student_details_bp)
app.register_blueprint(students_bp)
app.register_blueprint(update_student_bp)
