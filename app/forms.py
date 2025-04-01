# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    date = DateField('Data', validators=[DataRequired()], format='%Y-%m-%d')
    time = TimeField('Horário', validators=[DataRequired()], format='%H:%M')
    client = StringField('Cliente', validators=[DataRequired()])
    service = StringField('Serviço', validators=[DataRequired()])
    submit = SubmitField('Salvar')
    cancel = SubmitField('Cancelar')