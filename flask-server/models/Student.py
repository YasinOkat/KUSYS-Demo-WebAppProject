from main import db

# Defines the Student class, which is an SQLAlchemy object
class Student(db.Model):
    __tablename__ = 'students'

    student_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    # The relationship with the Course table, using course_student table
    courses = db.relationship('Course', secondary='course_student', back_populates='students')
