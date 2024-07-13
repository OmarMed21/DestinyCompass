from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired
from .professions import PROFESSIONS

class UserProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()], render_kw={"type": "number"})
    profession = SelectField('Profession', choices=[(prof, prof) for prof in PROFESSIONS], validators=[DataRequired()])
    goals = TextAreaField('Goals', validators=[DataRequired()])
    interests = SelectMultipleField('Interests', choices=[
        ('sports', 'Sports'),
        ('music', 'Music'),
        ('reading', 'Reading'),
        ('travel', 'Travel'),
    ])
    new_interest = StringField('New Interest')
    time_frame = SelectField('Time Frame', choices=[
        ('days', 'Days'),
        ('months', 'Months'),
        ('years', 'Years')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')
