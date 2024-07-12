from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class UserProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    profession = StringField('Profession', validators=[DataRequired()])
    goals = TextAreaField('Goals', validators=[DataRequired()])
    interests = TextAreaField('Interests', validators=[DataRequired()])
    time_frame = SelectField('Time Frame', choices=[('days', 'Days'), ('months', 'Months'), ('years', 'Years')], validators=[DataRequired()])
    submit = SubmitField('Submit')
