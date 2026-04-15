# ED System

Simple Flask and SQLite emergency department system for managing patients and related clinical activity.

## Features

- Register, edit, list, and delete patients
- Record ward admissions linked to a patient
- Record medicine administrations linked to a patient
- View dashboard counts for patients, active admissions, and medicines given today

## Database Tables

- `patients`: core patient demographic data
- `ward_admissions`: ward placement and admission reason for a patient
- `medicine_administrations`: medicines administered to a patient

## Main Pages

- `/`: dashboard
- `/add`: register a patient
- `/patients`: patient directory
- `/admissions`: ward admission form and log
- `/medications`: medicine administration form and log

## API Endpoints

- `GET /api/dashboard`
- `GET /api/patients`
- `GET /api/patients/<id>`
- `POST /api/patients`
- `PUT /api/patients/<id>`
- `DELETE /api/patients/<id>`
- `GET /api/admissions`
- `POST /api/admissions`
- `GET /api/medications`
- `POST /api/medications`

## Running the App

1. Install dependencies from `requirements.txt`.
2. Run `python app.py`.
3. Open the local Flask address shown in the terminal.

The app uses SQLite through Flask-SQLAlchemy. Missing tables are created automatically on startup.

## Live Deployment

This website is hosted on PythonAnywhere:

- https://audeallen.pythonanywhere.com/

## References

- AI assistance: GitHub Copilot (GPT-5.3-Codex)
- Flask documentation: https://flask.palletsprojects.com/
- Flask-SQLAlchemy documentation: https://flask-sqlalchemy.palletsprojects.com/
- SQLAlchemy documentation: https://docs.sqlalchemy.org/
- PythonAnywhere help docs: https://help.pythonanywhere.com/
- W3Schools Python tutorial: https://www.w3schools.com/python/
- W3Schools SQL tutorial: https://www.w3schools.com/sql/
- W3Schools JavaScript tutorial: https://www.w3schools.com/js/
- W3Schools HTML tutorial: https://www.w3schools.com/html/
- W3Schools CSS tutorial: https://www.w3schools.com/css/
