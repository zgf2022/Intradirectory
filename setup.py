from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '57e8728bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


config = {
	'appname':'IntraDirectory'
}

class listing(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	phonenumber = db.Column(db.String(25), nullable=True)
	contactname = db.Column(db.String(25), nullable=True)
	note = db.Column(db.String(200),nullable=True)

	def __repr__(self):
		return f"listing('{self.id}', '{self.phonenumber}', '{self.contactname}', '{self.note}')"

class settings(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	appname = db.Column(db.String(30), nullable=False)

db.create_all()