from flask import Blueprint
from controllers.BlogController import BlogController

blog_routes = Blueprint('blog_routes', __name__)

@blog_routes.route("/articles/list", methods=["GET"])
def index():
    return BlogController.index()

@blog_routes.route("/articles/delete/<int:article_id>", methods=["GET"])
def delete(article_id):
    return BlogController.delete(article_id)