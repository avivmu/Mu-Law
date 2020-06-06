from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length, Email


class VisitorForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(2, 16)])
    email = StringField('email', validators=[InputRequired(), Length(9, 36), Email()])
    text = TextAreaField('text', validators=[InputRequired(), Length(2, 200)])
