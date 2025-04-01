# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from app.config import Config

# Instâncias globais que serão inicializadas na aplicação
db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa extensões com a instância do app
    db.init_app(app)
    csrf.init_app(app)
    
    # Importa e registra o blueprint das rotas
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Cria as tabelas do banco de dados se elas não existirem
    with app.app_context():
        db.create_all()
        
    return app