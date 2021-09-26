from flask import render_template, request, session, redirect, url_for
from models.UsersModel import db, UsersModel
from passlib.hash import pbkdf2_sha256

class AuthController:
    def login():
        if session.get("user") is not None:
            return redirect(url_for("admin_routes.dashboard"))

        data = { "title": "Authorization" }
        return render_template("auth/login.html", params=data)

    def authorization():
        if session.get("user") is not None:
            return redirect(url_for("admin_routes.dashboard"))

        email = request.form["email"]
        password = request.form["password"]

        user_db = UsersModel.query.filter_by(email=email).first()

        if user_db is not None:
            if pbkdf2_sha256.verify(password, user_db.password):
                user = {
                    "login": user_db.login,
                    "email": user_db.email,
                    "role_id": 1
                }

                session["user"] = user
                return redirect(url_for('admin_routes.dashboard'))

        return redirect(url_for("login"))

    def register():
        if session.get("user") is not None:
            return redirect(url_for("admin_routes.dashboard"))

        data = { "title": "Register" }
        return render_template("auth/register.html", params=data)

    def user_register():
        if session.get("user") is not None:
            return redirect(url_for("admin_routes.dashboard"))

        user = {
            "login": request.form["login"],
            "email": request.form["email"],
            "role_id": 1
        }

        user_db = UsersModel(user=user, password=request.form["password"])
        db.session.add(user_db)
        db.session.commit()

        session["user"] = user
        
        return redirect(url_for("admin_routes.dashboard"))

    def logout():
        del session["user"]
        return redirect(url_for("auth_routes.login"))