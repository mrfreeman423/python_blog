from flask import Blueprint
from controllers.BlogController import BlogController

blog_routes = Blueprint('blog_routes', __name__)

@blog_routes.route("/articles/list", methods=["GET"])
def index():
    return BlogController.index()