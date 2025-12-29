from flask import Blueprint, render_template, redirect
from car_hire_core import db, Car, Customer

customer_bp = Blueprint("customer", __name__)

@customer_bp.route("/")
def home():
    customer = db.session.get(Customer, 1)
    cars = Car.query.all()
    return render_template("index.html", customer=customer, cars=cars)

@customer_bp.route("/rent/<int:car_id>")
def rent_car(car_id):
    car = db.session.get(Car, car_id)
    customer = db.session.get(Customer, 1)
    if car and car.available:
        car.available = False
        car.rented_by = customer.id
        db.session.commit()
    return redirect("/")

@customer_bp.route("/return/<int:car_id>")
def return_car(car_id):
    car = db.session.get(Car, car_id)
    if car and not car.available:
        car.available = True
        car.rented_by = None
        db.session.commit()
    return redirect("/")
