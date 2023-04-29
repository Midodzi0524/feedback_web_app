from flask import Blueprint, render_template,  request
from .models import User_data
from . import db
from .send_email import send_email

view = Blueprint("view", __name__)

@view.route('/')
def home():
    
    return render_template("home.html")




@view.route("/submit", methods=['POST'])
def Submit():
    customer = request.form['customer']
    dealer = request.form['dealer']
    rating = request.form['rating']
    comments = request.form['comments']
    
    if db.session.query(User_data).filter(User_data.customer == customer).count()==0:
        feedback = User_data(customer=customer, dealer=dealer,rating=rating,comments=comments)
        db.session.add(feedback)
        db.session.commit()
        send_email(customer,dealer,rating,comments)
    else:
        return render_template('home.html', message="You have already submitted feedback! ")
    

    return render_template("submit.html")


