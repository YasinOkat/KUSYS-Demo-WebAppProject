from flask import jsonify, Blueprint
from flask_login import login_required

from main import app
from models.Student import Student
from models.User import User

students_bp = Blueprint('students_bp', __name__)

# The route to get students info
@app.route('/students', methods=['GET'])
@login_required
def list_students():
    students = Student.query.all()
    students_data = []

    for student in students:
        user = User.query.get(student.user_id)
        if user:
            students_data.append({
                'student_id': student.student_id,
                'first_name': student.first_name,
                'last_name': student.last_name,
                'role': user.role,
                'username': user.username,
                'birth_date': student.birth_date.strftime('%Y-%m-%d')
            })

    return jsonify({'students': students_data})
