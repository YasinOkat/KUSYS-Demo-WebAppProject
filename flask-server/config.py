from flask_cors import CORS

from main import app

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/postgres'
app.config['SECRET_KEY'] = 'bd78312ee31cbd0b51586a57'