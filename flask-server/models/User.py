from flask_login import UserMixin

from main import bcrypt
from main import db
# Defines the User class, which is an SQLAlchemy object
class User(db.Model, UserMixin): # This inherits from UserMixIn, which is for the user authentication
    __tablename__ = 'users'  # Set the table name in the database

    # Columns in the table
    user_id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=True)

    # Initialize the object with username, password, and role
    def __init__(self, username, password, role=None):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode()  # Hash password using bcrypt
        self.role = role

    # Method to get the user's ID (required by UserMixin)
    def get_id(self):
        return str(self.user_id)

    # UserMixin properties for user authentication
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    # Method to check if the inputted password matches the user's hashed password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    # Static method to find a user by their username
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
