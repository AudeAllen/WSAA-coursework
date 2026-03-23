from flask import Flask, render_template, jsonify, request
from models import db, Patient, Admission

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ed_system.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/patients", methods=["GET"])
def get_patients():
    patients = Patient.query.all()
    return jsonify([patient.to_dict() for patient in patients])


@app.route("/api/patients", methods=["POST"])
def create_patient():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    required_fields = ["first_name", "last_name", "dob", "gender", "phone", "address"]

    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"{field} is required"}), 400

    patient = Patient(
        first_name=data["first_name"],
        last_name=data["last_name"],
        dob=data["dob"],
        gender=data["gender"],
        phone=data["phone"],
        address=data["address"]
    )

    db.session.add(patient)
    db.session.commit()

    return jsonify(patient.to_dict()), 201


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)