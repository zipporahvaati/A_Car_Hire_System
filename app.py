from flask import Flask
from config import Config
from car_hire_core import db
from routes.customer_routes import customer_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Register blueprints
app.register_blueprint(customer_bp)
app.register_blueprint(admin_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
