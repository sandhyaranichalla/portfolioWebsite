from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sandhyarani123@localhost:3000/portfolio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

# Initialize the app with SQLAlchemy
db.init_app(app)

# Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phonenumber = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    def __init__(self, name, phonenumber, email, age=None, gender=None):
        self.name = name
        self.phonenumber = phonenumber
        self.email = email
        self.age = age
        self.gender = gender


# Create database tables
with app.app_context():
    db.create_all()

# API Routes
@app.route("/")
def home():
    return render_template("base.html")

@app.route('/register', methods=['GET'])
def show_register_form():
    return render_template("registrationform.html")

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    phonenumber = data.get('phonenumber')
    email = data.get('email')
    age = data.get('age')
    gender = data.get('gender')

    if not name or not email:
        return jsonify({"error": "Name and Email are required"}), 400

    # Check if email already exists
    existing_user = Users.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 409
    new_user = Users(name=name, phonenumber=phonenumber, email=email, age=age, gender=gender)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
