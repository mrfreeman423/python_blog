from flask_sqlalchemy import SQLAlchemy
from models.UsersModel import UsersModel

db = SQLAlchemy()

class BlogModel(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), nullable=True)
    min_image = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(255), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    category_id = db.Column(db.Text(), nullable=True)
    author_id = db.Column(db.Integer(), db.ForeignKey(UsersModel.id), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    deleted_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self):
        pass

    def create():
        pass