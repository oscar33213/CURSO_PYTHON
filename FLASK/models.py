
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, name, email, passwd, is_admin=False):
        
        self.id = id
        self.name = name
        self.email = email
        self.passwd = passwd
        self.is_admin = is_admin
        
    def setPassword(self, passwd):
        self.passwd = generate_password_hash(passwd)
        
    def check_password(self, passwd):
        return check_password_hash(self.passwd,passwd)
    
    

users =  []


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None