from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RoomForm(FlaskForm):
    campusname = SelectField('Campus', choices=[('admin', 'admin'), ('khs', 'khs'), ('kms', 'kms'),
    	('kis', 'kis'), ('kes', 'kes'), ('kps', 'kps')], validators=[DataRequired()])
    primaryuse = SelectField('Primary users',choices=[('cte', 'cte'), ('sped', 'sped'), ('staff', 'staff'), ('generaled', 'generaled')], validators=[DataRequired()])
    roomname = StringField('Room Name', validators=[DataRequired()])
    submit = SubmitField('Add Room')

class ItemForm(FlaskForm):
	itemtype = SelectField('Type', validators=[DataRequired()])
	itemcondition = SelectField('Condition', choices=[('4','4'), ('3','3'), ('2','2'), ('1','1')], validators=[DataRequired()])
	itemnote = StringField('Note')
	itemquantity = StringField('Quantity - leave blank for 1')
	roomid = HiddenField()
	submit = SubmitField('Add Item')

class SettingsForm(FlaskForm):
	appname = StringField('Directory Title')
	submit = SubmitField('Save Changes')

class AddForm(FlaskForm):
	contactname = StringField('Contact Name')
	phonenumber = StringField('Phone Number or Extension')
	note = StringField('Practice or position')
	submit = SubmitField('Save Changes')

class SearchForm(FlaskForm):
	searchterm = StringField('Search')
	submit = SubmitField('Search')