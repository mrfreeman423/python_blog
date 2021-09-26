from flask import Blueprint
from controllers.AuthController import AuthController

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route("/login", methods=["GET"])
def login():
    return AuthController.login()

@auth_routes.route("/login", methods=["POST"])
def authorize():
    return AuthController.authorization()

@auth_routes.route("/register", methods=["GET"])
def register():
    return AuthController.register()

@auth_routes.route("/register", methods=["POST"])
def user_register():
    return AuthController.user_register()

@auth_routes.route("/logout")
def logout():
    return AuthController.logout()