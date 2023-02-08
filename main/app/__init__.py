from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from models import Product, ProductUser

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'

    db.init_app(app)
    migrate.init_app(app, db)


    return app

from app import models
