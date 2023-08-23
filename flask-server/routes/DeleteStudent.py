from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import login_required, current_user

from main import app, db
from models.CourseStudent import CourseStudent
from models.Student import Student
from models.User import User

delete_student_bp = Blueprint('delete_student_bp', __name__)


@app.route('/delete_student/<int:student_id>', methods=['POST'])
@login_required
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    if current_user.role == 'admin':
        try:
            user_id = student.user_id

            student_courses = CourseStudent.query.filter_by(student_id=student_id).all()
            for student_course in student_courses:
                db.session.delete(student_course)

            db.session.delete(student)

            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
            db.session.commit()
            return redirect(url_for("list_students"))
        except:
            return render_template("student_list.html")
