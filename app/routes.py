# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Appointment
from app.forms import AppointmentForm

# Criação do blueprint com o nome 'main'
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Obtém os filtros passados como parâmetros na URL
    date_filter = request.args.get('date')
    client_filter = request.args.get('client')
    service_filter = request.args.get('service')
    
    query = Appointment.query
    if date_filter:
        query = query.filter_by(date=date_filter)
    if client_filter:
        query = query.filter(Appointment.client.like(f'%{client_filter}%'))
    if service_filter:
        query = query.filter(Appointment.service.like(f'%{service_filter}%'))
        
    appointments = query.all()
    return render_template('appointment_list.html', appointments=appointments)

@bp.route('/appointment/new', methods=['GET', 'POST'])
def create_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(
            date = form.date.data,  
            time = form.time.data,  
            client = form.client.data,
            service = form.service.data
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Agendamento criado com sucesso!')
        return redirect(url_for('main.index'))
    return render_template('appointment_form.html', form=form, title='Novo Agendamento')

@bp.route('/appointment/edit/<int:id>', methods=['GET', 'POST'])
def edit_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    form = AppointmentForm(obj=appointment)
    if form.validate_on_submit():
        appointment.date = form.date.data
        appointment.time = form.time.data
        appointment.client = form.client.data
        appointment.service = form.service.data
        db.session.commit()
        flash('Agendamento atualizado com sucesso!')
        return redirect(url_for('main.index'))
    return render_template('appointment_form.html', form=form, title='Editar Agendamento')

@bp.route('/appointment/delete/<int:id>', methods=['POST'])
def delete_appointment(id):
    appointment = Appointment.query.get_or_404(id)
    db.session.delete(appointment)
    db.session.commit()
    flash('Agendamento excluído com sucesso!')
    return redirect(url_for('main.index'))
