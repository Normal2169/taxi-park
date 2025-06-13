from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from extensions import db
from distutils.util import strtobool
import models
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
@app.route("/")
def index():
    return render_template("index.html", current_page="main")
@app.route('/drivers')
def drivers():
    drivers = models.Drivers.query.all()
    return render_template('drivers.html', drivers=drivers,current_page="driver")
@app.route('/driver/add', methods=['POST'])
def add_Driver():
    if request.method == 'POST':
        Drivers = models.Drivers(
            full_name=request.form['full_name'],
            rating=request.form['rating'],
            is_available= strtobool(request.form['is_available']),
        )
        db.session.add(Drivers)
        db.session.commit()
        return redirect(url_for('drivers'))
@app.route("/driver/<int:id>", methods=["POST", "DELETE"])
def delete_Driver(id):
    if request.form.get('_method') == 'DELETE':
        driver = db.session.query(models.Drivers).filter(models.Drivers.id == id).first()
        db.session.delete(driver)
        db.session.commit()
        return redirect(url_for('drivers'))
    return "Метод не разрешён", 405
@app.route("/driver/edit/<int:id>", methods=["POST"])
def edit_driver_page(id):
    driver = db.session.query(models.Drivers).filter(models.Drivers.id == id).first()
    return render_template("driver_edit.html", driver=driver)
@app.route("/driver/update/<int:id>", methods=["POST"])
def update_driver(id):
    driver = db.session.query(models.Drivers).filter(models.Drivers.id == id).first()
    driver.full_name = request.form.get("full_name")
    driver.rating= request.form.get("rating")
    driver.is_available = strtobool(request.form['is_available'])
    db.session.commit()
    return redirect(url_for("drivers"))















@app.route('/cars')
def cars():
    cars = models.cars.query.all()
    return render_template('cars.html', cars=cars,current_page="cars")
@app.route('/cars/add', methods=['POST'])
def add_car():
    if request.method == 'POST':
        cars = models.cars(
            name = request.form.get("name"),
            manufacturer= request.form.get("manufacturer"),
            number = request.form.get("number"),
            color = request.form.get("color"),
            is_available = strtobool(request.form['is_available']),
        )
        db.session.add(cars)
        db.session.commit()
        return redirect(url_for('cars'))
@app.route("/car/<int:id>", methods=["POST", "DELETE"])
def delete_car(id):
    if request.form.get('_method') == 'DELETE':
        car = db.session.query(models.cars).filter(models.cars.id == id).first()
        db.session.delete(car)
        db.session.commit()
        return redirect(url_for('cars'))
    return "Метод не разрешён", 405
@app.route("/car/edit/<int:id>", methods=["POST"])
def edit_car_page(id):
    car = db.session.query(models.cars).filter(models.cars.id == id).first()
    return render_template("car_edit.html", car=car)
@app.route("/car/update/<int:id>", methods=["POST"])
def update_car(id):
    car = db.session.query(models.cars).filter(models.cars.id == id).first()
    car.name = request.form.get("name")
    car.manufacturer= request.form.get("manufacturer")
    car.number = request.form.get("number")
    car.color = request.form.get("color")
    car.is_available = strtobool(request.form['is_available'])
    db.session.commit()
    return redirect(url_for("cars"))















def main():
    app.run("0.0.0.0", port=8060, debug=True)
if __name__ == "__main__":
    main()