from extensions import db
class Drivers(db.Model):
    __tablename__ = 'Drivers'
    id = db.Column(db.Integer, primary_key=True)
    Full_Name = db.Column(db.String(100), nullable=False)
    Car = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True)
    def __repr__(self):
        return f'<Drivers {self.title}>'
class Orders(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    Client = db.Column(db.String(100), nullable=False)
    Date = db.Column(db.String(25), nullable=False)
    route =  db.Column(db.String(25), nullable=False)
    def __repr__(self):
        return f'<Orders {self.title}>'
class Cars(db.Model):
    __tablename__ = 'Cars'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Manufacturer = db.Column(db.String(100), nullable=False)
    Number = db.Column(db.String(100), nullable=False)
    Color = db.Column(db.String(25))
    def __repr__(self):
        return f'<Cars {self.title}>'