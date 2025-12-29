from flask import Blueprint, render_template, request, redirect
from car_hire_core import db, Car

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
def admin_dashboard():
    cars = Car.query.all()
    return render_template("admin.html", cars=cars)

@admin_bp.route("/admin/add_car", methods=["POST"])
def add_car():
    make = request.form["make"]
    model = request.form["model"]
    color = request.form["color"]
    new_car = Car(make=make, model=model, color=color)
    db.session.add(new_car)
    db.session.commit()
    return redirect("/admin")
