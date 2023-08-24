from flask import render_template, redirect, url_for, flash, Blueprint, jsonify
from flask_login import login_required, current_user
from sqlalchemy.exc import SQLAlchemyError

from main import app, db
from models.CourseStudent import CourseStudent
from models.Student import Student
from models.User import User

delete_student_bp = Blueprint('delete_student_bp', __name__)

# The route for deleteing a student
@app.route('/delete_student/<int:student_id>', methods=['POST'])
@login_required # Login required decorator for security
def delete_student(student_id):
    student = Student.query.get_or_404(student_id) # Gets the id of the student that is to be deleted
    response = {'success': False, 'message': 'An error occurred while deleting the student.'}
    if current_user.role != 'admin':
        response['message'] = "You don't have permission to delete this student."
        return jsonify(response)

    if current_user.role == 'admin': # Check if it's admin who sends the request
        try:
            user_id = student.user_id
            # First, deletes any records associated with the student in the student_courses table
            student_courses = CourseStudent.query.filter_by(student_id=student_id).all()
            for student_course in student_courses:
                db.session.delete(student_course)
            # Deletes the student from the students table
            db.session.delete(student)
            # Deletes the student from the users table
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)

            db.session.commit()
            response['success'] = True
            response['message'] = 'Student deleted successfully.'

            return jsonify(response)
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify(response)
        
    return jsonify(response)
