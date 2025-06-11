from extensions import db

class Drivers(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)
    def __repr__(self):
        return f'<Drivers {self.title}>'

class Cars(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    def __repr__(self):
        return f'<Cars {self.title}>'
    