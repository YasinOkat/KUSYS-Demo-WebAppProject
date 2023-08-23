from flask_login import UserMixin

from main import bcrypt
from main import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=True)

    def __init__(self, username, password, role=None):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode()
        self.role = role

    def get_id(self):
        return str(self.user_id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
