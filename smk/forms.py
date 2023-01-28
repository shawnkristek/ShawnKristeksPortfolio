from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
from wtforms.validators import DataRequired, Length, Email
import email_validator

class ContactForm(FlaskForm):
    name = TextField("Name", [DataRequired("Please enter your name.")])
    email = TextField("Email",[DataRequired("Please enter your email address."), Email("Please confirm your email address is correct.")])
    subject = TextField("Subject", [DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [Length(min=4, message=('Your message is too short.')), DataRequired("Please enter a message.")])
    submit = SubmitField("Send", [DataRequired("Please confirm you are human.")])
    recaptcha = RecaptchaField()