from flask import jsonify, Blueprint

from main import app
from models.Course import Course

courses_bp = Blueprint('courses_bp', __name__)


@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.get_all()
    courses_data = [course.serialize() for course in courses]
    return jsonify(courses_data)
