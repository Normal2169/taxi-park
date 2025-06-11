from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from extensions import db
import models
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
@app.route("/")
def index():
    return render_template("index.html", current_page="main")



@app.route('/Drivers')
def Drivers():
    Drivers = models.Drivers.query.all()
    return render_template('drivers.html', Drivers=Drivers)
@app.route('/Drivers/add', methods=['POST'])
def add_Drivers():
    if request.method == 'POST':
        Drivers = models.Drivers(
            Full_name=request.form['Full_name'],
            Car=request.form['Car'],
            raiting=request.form['raiting'],
            Color=request.form['Color']
        )
        db.session.add(Drivers)
        db.session.commit()
    return redirect(url_for('Drivers'))


def main():
    app.run("0.0.0.0", port=8060, debug=True)
if __name__ == "__main__":
    main()