from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from Db import db
from Db.models import users, articles
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key="123"
user_db = "aleksandra_knowledge_base_orm" 
host_ip="127.0.0.1"
host_port = "5432"
database_name = "knowledge_base_orm"
password = "1235"

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)