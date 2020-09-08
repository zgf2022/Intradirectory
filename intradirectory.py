from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import SettingsForm, AddForm, SearchForm

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

@app.route("/", methods=['GET', 'POST'])
def home():
	form = SearchForm()
	listings = listing.query
	if form.validate_on_submit():
		listings = listings.filter(listing.contactname.like('%' + form.searchterm.data + '%')| listing.phonenumber.like('%' + form.searchterm.data + '%')| listing.note.like('%' + form.searchterm.data + '%'))
		listings = listings.order_by(listing.contactname).all()
	else:
		listings = listing.query.all()
	return render_template('contactlist.html', form=form, config=config, listings=listings)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
	form = SearchForm()
	listings = listing.query
	if form.validate_on_submit():
		listings = listings.filter(listing.contactname.like('%' + form.searchterm.data + '%')| listing.phonenumber.like('%' + form.searchterm.data + '%')| listing.note.like('%' + form.searchterm.data + '%'))
		listings = listings.order_by(listing.contactname).all()
	else:
		listings = listing.query.all()
	return render_template('admincontactlist.html', form=form, config=config, listings=listings)



@app.route("/addcontact", methods=['GET', 'POST'])
def addcontact():
	form = AddForm()
	if form.validate_on_submit():
		listingdb = listing(contactname=form.contactname.data, phonenumber=form.phonenumber.data, note=form.note.data)
		db.session.add(listingdb)
		db.session.commit()
		flash('Listing added', 'success')
		return redirect("/admin")
	return render_template('newcontact.html', title='New Contact',
						   form=form, legend='New Contact', config=config)

@app.route("/editcontact", methods=['GET', 'POST'])
def editcontact():
	listid = request.form.get("listid")
	item = db.session.query(listing).get(listid)
	form = AddForm(obj=item)
	if form.validate_on_submit():
		form.populate_obj(item)
		db.session.add(item)
		db.session.commit()
		flash('Listing edited', 'success')
		return redirect("/admin")
	return render_template('newcontact.html', title='New Contact',
						   form=form, listid=listid, legend='New Contact', config=config)

@app.route("/deletecontact", methods=['GET', 'POST'])
def deletecontact():
	listid = request.form.get("listid")
	item = db.session.query(listing).get(listid)
	db.session.delete(item)
	db.session.commit()
	flash('Listing Deleted', 'success')
	return redirect("/admin")

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
