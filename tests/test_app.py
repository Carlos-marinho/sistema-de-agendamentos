# tests/test_app.py
import pytest
import datetime
import sys
import os
from app import create_app, db
from app.models import Appointment


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,  # Desabilita CSRF para os testes
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_appointment(client, app):
    # Envia dados via formulário (os campos de data e hora são strings que o Flask-WTF converte)
    response = client.post('/appointment/new', data={
        'date': '2025-04-01',
        'time': '10:00',
        'client': 'Carlos',
        'service': 'Consulta'
    }, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        appointment = Appointment.query.filter_by(client='Carlos').first()
        assert appointment is not None

def test_edit_appointment(client, app):
    with app.app_context():
        # Cria o agendamento utilizando objetos do tipo date e time
        appointment = Appointment(
            date=datetime.date(2025, 4, 1),
            time=datetime.time(10, 0),
            client='Carlos',
            service='Consulta'
        )
        db.session.add(appointment)
        db.session.commit()
        appointment_id = appointment.id

    response = client.post(f'/appointment/edit/{appointment_id}', data={
        'date': '2025-04-02',
        'time': '11:00',
        'client': 'Carlos Marinho',
        'service': 'Consulta Médica'
    }, follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        # Usando Session.get() para evitar o aviso de legacy API
        appointment = db.session.get(Appointment, appointment_id)
        assert appointment.client == 'Carlos Marinho'

def test_delete_appointment(client, app):
    with app.app_context():
        appointment = Appointment(
            date=datetime.date(2025, 4, 1),
            time=datetime.time(10, 0),
            client='Carlos',
            service='Consulta'
        )
        db.session.add(appointment)
        db.session.commit()
        appointment_id = appointment.id

    response = client.post(f'/appointment/delete/{appointment_id}', follow_redirects=True)
    assert response.status_code == 200

    with app.app_context():
        appointment = db.session.get(Appointment, appointment_id)
        assert appointment is None
