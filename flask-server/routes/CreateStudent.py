from flask import render_template, request, redirect, url_for, flash, Blueprint, jsonify
from flask_login import login_required, current_user

from forms.CreateUserForm import CreateUserForm
from main import app, db
from models.Student import Student
from models.User import User

create_student_bp = Blueprint('create_student_bp', __name__)


@app.route('/create_student', methods=['GET', 'POST'])
@login_required
def create_student():
    user_form = CreateUserForm()

    if current_user.role == 'admin':
        if request.method == 'POST':
            new_user = User(
                username=user_form.username.data,
                password=user_form.password.data,
                role='admin' if request.json.get('isAdmin') else 'user'  # Set role based on isAdmin value
            )
            db.session.add(new_user)
            db.session.commit()

            new_student = Student(
                user_id=new_user.user_id,
                first_name=user_form.first_name.data,
                last_name=user_form.last_name.data,
                birth_date=user_form.birth_date.data
            )
            db.session.add(new_student)
            db.session.commit()

            return redirect(url_for('list_students'))

    return jsonify(message='Permission denied'), 403  # HTTP 403 Forbidden

