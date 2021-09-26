from models.UsersModel import db
from flask import Flask, session, render_template, url_for, redirect
from controllers.AuthController import AuthController
from controllers.AdminController import AdminController
from controllers.BlogController import BlogController
from routes.auth import auth_routes
from routes.admin import admin_routes
from routes.blog import blog_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://blog:password@localhost:5432/blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Routes
app.register_blueprint(auth_routes)
app.register_blueprint(admin_routes)
app.register_blueprint(blog_routes)

@app.route("/")
def index():
    data = { "title": "Welcome to my custom blog!" }
    return render_template("index.html", params=data)

with app.test_request_context():
    url_for('static', filename='style.css')