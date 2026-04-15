from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Core patient profile table used throughout the app.
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
    ward_admissions = db.relationship(
        "WardAdmission",
        back_populates="patient",
        cascade="all, delete-orphan",
        lazy=True,
    )
    medicine_administrations = db.relationship(
        "MedicineAdministration",
        back_populates="patient",
        cascade="all, delete-orphan",
        lazy=True,
    )

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


class WardAdmission(db.Model):
    __tablename__ = "ward_admissions"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    ward_name = db.Column(db.String(100), nullable=False)
    bed_number = db.Column(db.String(20), nullable=True)
    admission_reason = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Admitted")
    admitted_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    discharged_at = db.Column(db.DateTime, nullable=True)

    patient = db.relationship("Patient", back_populates="ward_admissions")

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "patient_name": f"{self.patient.first_name} {self.patient.last_name}",
            "ward_name": self.ward_name,
            "bed_number": self.bed_number,
            "admission_reason": self.admission_reason,
            "status": self.status,
            "admitted_at": self.admitted_at.isoformat(),
            "discharged_at": self.discharged_at.isoformat() if self.discharged_at else None,
        }


class MedicineAdministration(db.Model):
    __tablename__ = "medicine_administrations"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    medicine_name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    route = db.Column(db.String(50), nullable=False)
    administered_by = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    administered_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Each medication event belongs to one patient.
    patient = db.relationship("Patient", back_populates="medicine_administrations")

    def to_dict(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "patient_name": f"{self.patient.first_name} {self.patient.last_name}",
            "medicine_name": self.medicine_name,
            "dosage": self.dosage,
            "route": self.route,
            "administered_by": self.administered_by,
            "notes": self.notes,
            "administered_at": self.administered_at.isoformat(),
        }

# References:
# - AI assistance: GitHub Copilot (GPT-5.3-Codex)
# - Flask-SQLAlchemy documentation: https://flask-sqlalchemy.palletsprojects.com/
# - SQLAlchemy ORM relationships: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
# - W3Schools SQL tutorial: https://www.w3schools.com/sql/
# - Real Python SQLAlchemy guide: https://realpython.com/python-sqlite-sqlalchemy/