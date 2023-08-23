from flask import request, jsonify, Blueprint
from flask_login import login_required, current_user

from main import app, db
from models.Course import Course
from models.Student import Student

select_courses_bp = Blueprint('select_courses_bp', __name__)


@app.route('/select_courses/<int:student_id>', methods=['POST'])
@login_required
def select_courses(student_id):
    student = Student.query.get_or_404(student_id)

    # Ensure that the logged-in user can only select courses for their own profile
    if current_user.role == 'admin' or current_user.user_id == student.user_id:
        if request.method == 'POST':
            data = request.json
            selected_course_ids = data.get('selected_courses', [])
            selected_courses = Course.query.filter(Course.course_id_pk.in_(selected_course_ids)).all()

            student.courses = selected_courses
            db.session.commit()

            return jsonify(message='Courses selected successfully')

        return jsonify(error='Invalid request')

    return jsonify(error='Unauthorized')
