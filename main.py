from flask import Flask
from src.auth.controller import urls_blueprint as url1
from flask_sqlalchemy import SQLAlchemy

# from urls2 import urls2_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

# register routes from urls
app.register_blueprint(url1)
# we can register routes with specific prefix
# app.register_blueprint(urls2_blueprint, url_prefix='/urls2')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)