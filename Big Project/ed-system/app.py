from datetime import date

from flask import Flask, render_template, jsonify, request

from models import db, Patient, WardAdmission, MedicineAdministration

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ed_system.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# Page routes render the main UI views.
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_page():
    return render_template("add_patient.html", today=date.today().isoformat())


@app.route("/patients")
def patients_page():
    return render_template("patients.html")


@app.route("/admissions")
def admissions_page():
    patients = Patient.query.order_by(Patient.last_name, Patient.first_name).all()
    return render_template("admissions.html", patients=patients)


@app.route("/medications")
def medications_page():
    patients = Patient.query.order_by(Patient.last_name, Patient.first_name).all()
    return render_template("medications.html", patients=patients)


# Helper to normalize required text fields from incoming JSON.
def get_required_text(data, field_name):
    value = data.get(field_name)

    if value is None or not str(value).strip():
        return None

    return str(value).strip()


def get_patient_or_404(patient_id):
    patient = db.session.get(Patient, patient_id)

    if patient is None:
        return None, (jsonify({"error": "Patient not found"}), 404)

    return patient, None


# Dashboard endpoint returns quick summary numbers for the home page cards.
@app.route("/api/dashboard", methods=["GET"])
def get_dashboard_stats():
    total_patients = Patient.query.count()
    active_admissions = WardAdmission.query.filter_by(status="Admitted").count()
    today = date.today().isoformat()

    todays_admissions = WardAdmission.query.filter(
        db.func.date(WardAdmission.admitted_at) == today
    ).count()
    todays_medicines = MedicineAdministration.query.filter(
        db.func.date(MedicineAdministration.administered_at) == today
    ).count()

    return jsonify(
        {
            "total_patients": total_patients,
            "active_admissions": active_admissions,
            "todays_admissions": todays_admissions,
            "todays_medicines": todays_medicines,
        }
    )


# Patient CRUD endpoints.
@app.route("/api/patients", methods=["GET"])
def get_patients():
    patients = Patient.query.all()
    result = []

    for patient in patients:
        result.append(patient.to_dict())

    return jsonify(result)


@app.route("/api/patients/<int:id>", methods=["GET"])
def get_one_patient(id):
    patient = db.session.get(Patient, id)

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
    patient = db.session.get(Patient, id)

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
    patient = db.session.get(Patient, id)

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()

    return jsonify({"message": "Patient deleted"})


# Ward admission log endpoints.
@app.route("/api/admissions", methods=["GET"])
def get_admissions():
    admissions = WardAdmission.query.order_by(WardAdmission.admitted_at.desc()).all()
    return jsonify([admission.to_dict() for admission in admissions])


@app.route("/api/admissions", methods=["POST"])
def add_admission():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No data sent"}), 400

    patient_id = data.get("patient_id")
    ward_name = get_required_text(data, "ward_name")
    admission_reason = get_required_text(data, "admission_reason")
    bed_number = get_required_text(data, "bed_number")

    if not patient_id:
        return jsonify({"error": "patient_id is required"}), 400

    if ward_name is None or admission_reason is None:
        return jsonify({"error": "ward_name and admission_reason are required"}), 400

    patient, error_response = get_patient_or_404(patient_id)
    if error_response:
        return error_response

    admission = WardAdmission(
        patient_id=patient.id,
        ward_name=ward_name,
        bed_number=bed_number,
        admission_reason=admission_reason,
    )

    db.session.add(admission)
    db.session.commit()

    return jsonify(admission.to_dict()), 201


# Medication administration log endpoints.
@app.route("/api/medications", methods=["GET"])
def get_medications():
    medications = MedicineAdministration.query.order_by(
        MedicineAdministration.administered_at.desc()
    ).all()
    return jsonify([medication.to_dict() for medication in medications])


@app.route("/api/medications", methods=["POST"])
def add_medication():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No data sent"}), 400

    patient_id = data.get("patient_id")
    medicine_name = get_required_text(data, "medicine_name")
    dosage = get_required_text(data, "dosage")
    route = get_required_text(data, "route")
    administered_by = get_required_text(data, "administered_by")
    notes = get_required_text(data, "notes")

    if not patient_id:
        return jsonify({"error": "patient_id is required"}), 400

    if None in (medicine_name, dosage, route, administered_by):
        return jsonify({"error": "medicine_name, dosage, route, and administered_by are required"}), 400

    patient, error_response = get_patient_or_404(patient_id)
    if error_response:
        return error_response

    medication = MedicineAdministration(
        patient_id=patient.id,
        medicine_name=medicine_name,
        dosage=dosage,
        route=route,
        administered_by=administered_by,
        notes=notes,
    )

    db.session.add(medication)
    db.session.commit()

    return jsonify(medication.to_dict()), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# References:
# - AI assistance: GitHub Copilot (GPT-5.3-Codex)
# - Flask documentation: https://flask.palletsprojects.com/
# - Flask-SQLAlchemy documentation: https://flask-sqlalchemy.palletsprojects.com/
# - SQLAlchemy ORM documentation: https://docs.sqlalchemy.org/
# - W3Schools Python tutorial: https://www.w3schools.com/python/
# - PythonAnywhere help docs: https://help.pythonanywhere.com/