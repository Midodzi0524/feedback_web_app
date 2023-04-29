from . import db


class User_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(150), unique=True)
    dealer = db.Column(db.String(150))
    rating = db.Column(db.Integer)
    comments= db.Column(db.Text())
    

    
    