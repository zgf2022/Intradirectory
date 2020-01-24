from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RoomForm, ItemForm, SettingsForm

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
	username = db.Column(db.String(25), nullable=True)

@app.route("/")
def home():
    return render_template('main.html', config=config)

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
