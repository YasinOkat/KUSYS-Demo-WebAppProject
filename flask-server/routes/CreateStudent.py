from flask import render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask_login import login_required, current_user

from forms.CreateUserForm import CreateUserForm
from main import app, db
from models.Student import Student
from models.User import User

create_student_bp = Blueprint('create_student_bp', __name__)

# The route for creating a student
# The route for creating a student
@app.route('/create_student', methods=['GET', 'POST'])
@login_required # Login required decorator for security
def create_student():
    user_form = CreateUserForm()
    response = {'success': False, 'message': 'Permission denied'}

    if current_user.role == 'admin': # Check if the logged in user is admin
        if request.method == 'POST':
            # Check if the username already exists in the database
            existing_user = User.query.filter_by(username=user_form.username.data).first()
            if existing_user:
                return jsonify(message='Username already exists'), 400  # HTTP 400 Bad Request
            
            # Create a new user
            new_user = User(
                username=user_form.username.data,
                password=user_form.password.data,
                role='admin' if request.json.get('isAdmin') else 'user' 
            )
            db.session.add(new_user)
            db.session.commit()

            # Create a new student
            new_student = Student(
                user_id=new_user.user_id,
                first_name=user_form.first_name.data,
                last_name=user_form.last_name.data,
                birth_date=user_form.birth_date.data
            )
            db.session.add(new_student)
            db.session.commit()
            response['success'] = True
            response['message'] = 'Student created successfully'
            return response


    return jsonify(message='Permission denied'), 403  # HTTP 403 Forbidden
