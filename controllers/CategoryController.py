from flask import render_template, request, session, redirect, url_for

class CategoryController():
    def list():
        if session.get("user") is None:
            return redirect(url_for("auth_routes.login"))