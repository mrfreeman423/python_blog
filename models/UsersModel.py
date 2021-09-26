from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)
    role_id = db.Column(db.Integer(), nullable=False)

    def __init__(self, user, password):
        self.login = user["login"]
        self.email = user["email"]
        self.password = password
        self.role_id = user["role_id"]