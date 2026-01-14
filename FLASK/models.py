

from flask_login import UserMixin, LoginManager

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
login_manager = LoginManager()

class User(UserMixin, db.Model):
    
    __tablename__ = 'Usuarios_pagina'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    is_admin = db.Column(db.Boolean, default = False)
        
    def setPassword(self, password):
        self.passwd = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)




