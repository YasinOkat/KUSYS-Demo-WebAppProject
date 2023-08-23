from main import db


class Course(db.Model):
    __tablename__ = 'courses'

    course_id_pk = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(100), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)

    students = db.relationship('Student', secondary='course_student', back_populates='courses')

    def __init__(self, course_name):
        self.course_name = course_name

    def serialize(self):
        return {
            'course_id_pk': self.course_id_pk,
            'course_id': self.course_id,
            'course_name': self.course_name
        }

    @staticmethod
    def create(course_name):
        new_course = Course(course_name=course_name)
        db.session.add(new_course)
        db.session.commit()
        return new_course

    @staticmethod
    def get_all():
        return Course.query.all()
