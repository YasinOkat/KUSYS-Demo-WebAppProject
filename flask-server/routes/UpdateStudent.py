from flask import request, Blueprint, jsonify
from flask_login import login_required, current_user

from forms.UpdateStudentForm import UpdateStudentForm
from main import app, db
from models.Student import Student
from models.User import User

update_student_bp = Blueprint('update_student_bp', __name__)

# The route to update a student
@app.route('/update_student/<int:student_id>', methods=['GET', 'POST'])
@login_required
def update_student(student_id):
    response = {'success': False, 'message': 'Unauthorized'}

    student = Student.query.get_or_404(student_id)
    form = UpdateStudentForm()

    if current_user.role == 'admin':  # Only admin can update
        if request.method == 'POST':
            student.first_name = form.first_name.data
            student.last_name = form.last_name.data
            student.birth_date = form.birth_date.data
            db.session.commit()

            # Update corresponding User record
            user = User.query.get(student.user_id)
            if user:
                user.username = form.username.data
                user.role = 'admin' if request.json.get('isAdmin') else 'user'
                db.session.commit()

            response['success'] = True
            response['message'] = 'Student updated successfully'
        else:
            response['message'] = 'Provide the required data via POST request'
    else:
        response['message'] = 'Unauthorized'

    return jsonify(response)