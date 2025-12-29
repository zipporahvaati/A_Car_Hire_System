from .db import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rented_cars = db.relationship('Car', backref='customer', lazy=True)

    def __repr__(self):
        return f"<Customer {self.name}>"

class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    available = db.Column(db.Boolean, default=True)
    rented_by = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.color}) - {'Available' if self.available else 'Not Available'}"
