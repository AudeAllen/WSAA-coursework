from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    admissions = db.relationship("Admission", backref="patient", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
            "gender": self.gender,
            "phone": self.phone,
            "address": self.address,
            "created_at": self.created_at.isoformat()
        }


class Admission(db.Model):
    __tablename__ = "admissions"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    admission_time = db.Column(db.DateTime, default=datetime.utcnow)
    chief_complaint = db.Column(db.String(200), nullable=False)
    triage_level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Waiting")
    doctor_name = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    discharge_time = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "admission_time": self.admission_time.isoformat(),
            "chief_complaint": self.chief_complaint,
            "triage_level": self.triage_level,
            "status": self.status,
            "doctor_name": self.doctor_name,
            "notes": self.notes,
            "discharge_time": self.discharge_time.isoformat() if self.discharge_time else None
        }