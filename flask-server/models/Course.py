from main import db  # Import the database instance (assuming it's named "db")

# Defines the Course class, which is an SQLAlchemy object
class Course(db.Model):
    __tablename__ = 'courses'  # Sets the table name

    # The columns in the courses table
    course_id_pk = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(100), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)

    # Sets the relationship with thie Student table using the course_student table
    students = db.relationship('Student', secondary='course_student', back_populates='courses')

    # Initialize the object
    def __init__(self, course_name):
        self.course_name = course_name

    # Serialize method to convert the object to a dictionary
    def serialize(self):
        return {
            'course_id_pk': self.course_id_pk,
            'course_id': self.course_id,
            'course_name': self.course_name
        }

    # The method to create a new course, and then add it to the database
    @staticmethod
    def create(course_name):
        new_course = Course(course_name=course_name)
        db.session.add(new_course)
        db.session.commit()
        return new_course

    # Static method to retrieve all courses from the database
    @staticmethod
    def get_all():
        return Course.query.all()