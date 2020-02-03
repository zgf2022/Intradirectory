from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import SettingsForm, AddForm

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

	def __repr__(self):
		return f"listing('{self.id}', '{self.phonenumber}', '{self.contactname}')"

class settings(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	appname = db.Column(db.String(30), nullable=False)

@app.route("/")
def home():
	listings = listing.query.all()
	return render_template('contactlist.html', config=config, listings=listings)

@app.route("/addcontact", methods=['GET', 'POST'])
def addcontact():
	form = AddForm()
	if form.validate_on_submit():
		listingdb = listing(contactname=form.contactname.data, phonenumber=form.phonenumber.data)
		db.session.add(listingdb)
		db.session.commit()
		flash('Listing added', 'success')
		return redirect("/")
	return render_template('newcontact.html', title='New Contact',
						   form=form, legend='New Contact', config=config)

@app.route("/settings", methods=['GET', 'POST'])
def settings():
	form = SettingsForm()
	if form.validate_on_submit():
		config["appname"] = form.appname.data
		flash('Settings Saved', 'success')
		return redirect('/settings')
	return render_template('settings.html', title='Settings',
								form=form, legend='Settings', config=config)
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
