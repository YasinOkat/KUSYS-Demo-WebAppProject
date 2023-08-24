from models.Course import Course
from main import db 

def create_seed_data():

    courses = [
        Course(course_id='CSI101', name='Introduction to Computer Science'),
        Course(course_id='CSI102', name='Algorithms'),
        Course(course_id='MAT101', name='Calculus'),
        Course(course_id='PHY101', name='Physics')
    ]

    db.session.add_all(courses)
    db.session.commit()

# Call the function to populate the initial data
create_seed_data()
