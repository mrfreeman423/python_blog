from flask import Blueprint
from controllers.AdminController import AdminController
from controllers.BlogController import BlogController

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route("/admin/dashboard")
def dashboard():
    return AdminController.dashboard()

@admin_routes.route("/admin/blog/create")
def create():
    return BlogController.create()