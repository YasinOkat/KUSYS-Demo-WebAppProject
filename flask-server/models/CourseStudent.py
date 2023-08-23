from main import db


class CourseStudent(db.Model):
    __tablename__ = 'course_student'

    course_student_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id_pk'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
