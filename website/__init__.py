from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_NAME = 'database.db'



#'postgresql://postgres:Monica123@localhost/user_data'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']= "GDHNDKAND JAK"
    app.config["SQLALCHEMY_DATABASE_URI"]=f'sqlite:///{DB_NAME}'
    db.init_app(app)

    
    from .view import view
    from .send_email import send_email
    
    app.register_blueprint(view, url_prefix='/')
    
    
    
   
    
    create_database(app)
    
    
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()

    
