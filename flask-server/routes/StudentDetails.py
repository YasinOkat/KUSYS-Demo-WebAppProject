from flask import jsonify, Blueprint
from flask_login import login_required

from main import app
from models.Student import Student
from models.User import User

student_details_bp = Blueprint('student_details_bp', __name__)

# The route to get student details
@app.route('/student_details/<int:student_id>', methods=['GET'])
@login_required # The login_required decorator for safety
def student_details(student_id):
    student = Student.query.get(student_id)
    if student:
        serialized_courses = [course.serialize() for course in student.courses]  # Serialize courses
        user = User.query.get(student.user_id)  # Get the associated User object
        if user:
            # Return the details in json
            return jsonify({
                'student_id': student.user_id,
                'username': user.username,
                'first_name': student.first_name,
                'role': user.role,
                'last_name': student.last_name,
                'birth_date': student.birth_date.strftime('%Y-%m-%d'),
                'courses': serialized_courses
            })
        else:
            return jsonify({'error': 'User not found'}), 404
    return jsonify({'error': 'Student not found'}), 404
