from flask import session, redirect, url_for, render_template, request

class AdminController:
    def dashboard():
        if session.get("user") is None:
            return redirect(url_for("login"))

        data = { "title": "Welcome to dashboard!", "user": session["user"] }
        return render_template("admin/dashboard.html", params=data)