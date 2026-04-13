from flask import Flask, render_template, jsonify, request
from models import db, Patient

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ed_system.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_page():
    return render_template("add_patient.html")


@app.route("/patients")
def patients_page():
    return render_template("patients.html")


@app.route("/api/patients", methods=["GET"])
def get_patients():
    patients = Patient.query.all()
    result = []

    for patient in patients:
        result.append(patient.to_dict())

    return jsonify(result)


@app.route("/api/patients/<int:id>", methods=["GET"])
def get_one_patient(id):
    patient = Patient.query.get(id)

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    return jsonify(patient.to_dict())


@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No data sent"}), 400

    new_patient = Patient(
        first_name=data["first_name"],
        last_name=data["last_name"],
        dob=data["dob"],
        gender=data["gender"],
        phone=data["phone"],
        address=data["address"]
    )

    db.session.add(new_patient)
    db.session.commit()

    return jsonify(new_patient.to_dict()), 201


@app.route("/api/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    patient = Patient.query.get(id)

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    data = request.get_json()

    if data is None:
        return jsonify({"error": "No data sent"}), 400

    # Only update fields that are provided and not empty
    if "first_name" in data and data["first_name"].strip():
        patient.first_name = data["first_name"]
    if "last_name" in data and data["last_name"].strip():
        patient.last_name = data["last_name"]
    if "dob" in data and data["dob"].strip():
        patient.dob = data["dob"]
    if "gender" in data and data["gender"].strip():
        patient.gender = data["gender"]
    if "phone" in data and data["phone"].strip():
        patient.phone = data["phone"]
    if "address" in data and data["address"].strip():
        patient.address = data["address"]

    db.session.commit()

    return jsonify(patient.to_dict())


@app.route("/api/patients/<int:id>", methods=["DELETE"])
def delete_patient(id):
    patient = Patient.query.get(id)

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()

    return jsonify({"message": "Patient deleted"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)