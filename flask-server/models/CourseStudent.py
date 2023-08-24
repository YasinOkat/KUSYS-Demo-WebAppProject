from main import db

# Defines the CourseStudent class, which is an SQLAlchemy object
class CourseStudent(db.Model):
    __tablename__ = 'course_student' # Sets the table name

    # The columns
    course_student_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id_pk'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
