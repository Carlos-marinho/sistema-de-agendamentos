# app/models.py
from app import db
from datetime import date, time

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)  # Formato 'DD-MM-YYYY'
    time = db.Column(db.Time, nullable=False)   # Formato 'HH:MM'
    client = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'(Agendamento {self.id} - {self.client})'
