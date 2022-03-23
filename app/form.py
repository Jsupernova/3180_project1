from random import choices
from secrets import choice
from wsgiref.validate import validator
from xml.dom.minicompat import StringTypes
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired,FileAllowed
from wtforms import StringField,TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired
class PropertyForm(FlaskForm):
    property_name = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms_num = IntegerField('No. of Rooms', validators=[DataRequired()])
    bathrooms_num = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('House','House'), ('Apartment','Apartment')])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])