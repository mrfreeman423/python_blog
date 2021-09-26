from flask import render_template, request, session, redirect, url_for
from models.BlogModel import db, BlogModel

class BlogController:
    def index():
        data = { "title": "Список опубликованных статей" }

        list_articles = BlogModel.query.all()
        data["list_articles"] = list_articles

        return render_template("admin/articles/index.html", params=data)

    def publish():
        pass

    def change():
        pass

    def change_store():
        pass

    def create():
        if session.get("user") is None:
            return redirect(url_for("auth_routes.login"))

        data = { "title": "Создание новой статьи" }
        return render_template("admin/blog/create.html", params=data)

    def store():
        if session.get("user") is None:
            return redirect(url_for("auth_routes.login"))

    def delete():
        

        