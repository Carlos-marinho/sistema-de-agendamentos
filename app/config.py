# app/config.py
class Config:
    SECRET_KEY = 'teste-sistema-agendamento'
    # Utilizando um arquivo SQLite no diretório do projeto (arquivo será criado automaticamente)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///agendamento.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
