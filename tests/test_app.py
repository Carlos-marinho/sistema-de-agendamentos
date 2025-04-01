# tests/test_app.py
import unittest
from app import create_app, db
from app.models import Appointment

class AppointmentTestCase(unittest.TestCase):
    def setUp(self):
        # Cria a aplicação de teste e configura o banco em memória
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()
    
    def tearDown(self):
        # Remove o banco após os testes
        with self.app.app_context():
            db.drop_all()
            
    def test_create_appointment(self):
        # Testa a criação de um agendamento via POST
        response = self.client.post('/appointment/new', data={
            'date': '2025-04-01',
            'time': '10:00',
            'client': 'João',
            'service': 'Consulta'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            appointment = Appointment.query.filter_by(client='João').first()
            self.assertIsNotNone(appointment)
            
    def test_edit_appointment(self):
        with self.app.app_context():
            appointment = Appointment(date='2025-04-01', time='10:00', client='João', service='Consulta')
            db.session.add(appointment)
            db.session.commit()
            appointment_id = appointment.id
        
        response = self.client.post(f'/appointment/edit/{appointment_id}', data={
            'date': '2025-04-02',
            'time': '11:00',
            'client': 'João Edited',
            'service': 'Consulta Edited'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            appointment = Appointment.query.get(appointment_id)
            self.assertEqual(appointment.client, 'João Edited')
            
    def test_delete_appointment(self):
        with self.app.app_context():
            appointment = Appointment(date='2025-04-01', time='10:00', client='João', service='Consulta')
            db.session.add(appointment)
            db.session.commit()
            appointment_id = appointment.id
        
        response = self.client.post(f'/appointment/delete/{appointment_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            appointment = Appointment.query.get(appointment_id)
            self.assertIsNone(appointment)
            
if __name__ == '__main__':
    unittest.main()
