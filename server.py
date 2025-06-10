from flask import Flask, render_template, request
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
def main():
    app.run("0.0.0.0", port=8060, debug=True)
if __name__ == "__main__":
    main()


@app.route('/Cars')
def Cars():
    Cars = models.Cars.query.all()
    return render_template('сars.html', Cars=Cars)
@app.route('/Cars/add', methods=['POST'])
def add_Cars():
    if request.method == 'POST':
        Cars = models.Cars(
            Name=request.form['Name'],
            Manufacturer=request.form['Manufacturer'],
            Number=request.form['Number'],
            Color=request.form['Color']
        )
        db.session.add(Cars)
        db.session.commit()
        return redirect(url_for('Cars'))