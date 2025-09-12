from flask import render_template, request, redirect, url_for
from ..models import db, User

class UserController:

    @staticmethod
    def list_users():
        users = User.query.all()
        return render_template("users.html", users=users)

    @staticmethod
    def create_user():
        if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("bd_user.list_users"))  # blueprint + método

        return render_template("create_user.html")

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for("bd_user.list_users"))  # blueprint + método
