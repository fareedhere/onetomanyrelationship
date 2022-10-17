from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///exam.sqlite3'
db=SQLAlchemy(app)

class Owner(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(100))
    pets=db.relationship('Pet',backref='owner')



class Pet(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    age=db.Column(db.Integer)
    ownerid=db.Column(db.Integer,db.ForeignKey('owner.id'))