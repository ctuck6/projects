from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.database import User

class RegistrationForm(FlaskForm):
	username = StringField("Username", validators = [DataRequired(), Length(min = 4, max = 20)])
	email = StringField("Email", validators = [DataRequired(), Email()])
	password = PasswordField("Password", validators = [DataRequired()])
	confirmPassword = PasswordField("Re-Enter Password", validators = [DataRequired(), EqualTo("password")])
	submit = SubmitField("Sign Up")

	def validate_username(self, username):
		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError("Username already exists. Please try again.")

	def validate_email(self, email):
		user = User.query.filter_by(email = email.data).first()
		if user:
			raise ValidationError("Email already exists. Please try again.")

class LoginForm(FlaskForm):
	email = StringField("Email", validators = [DataRequired(), Email()])
	password = PasswordField("Password", validators = [DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")

class UpdateAccountForm(FlaskForm):
	username = StringField("Username", validators = [DataRequired(), Length(min = 4, max = 20)])
	email = StringField("Email", validators = [DataRequired(), Email()])
	profilePicture = FileField("Update Profile Picture", validators = [FileAllowed(["jpeg", "png", "jpg"])])
	submit = SubmitField("Save Changes")

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username = username.data).first()
			if user:
				raise ValidationError("Username already exists. Please try again.")

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email = email.data).first()
			if user:
				raise ValidationError("Email already exists. Please try again.")

class ReviewForm(FlaskForm):
	title = StringField("Title", validators = [DataRequired()])
	body = TextAreaField("Content", validators = [DataRequired()])
	submit = SubmitField("Post Review")

class RequestResetForm(FlaskForm):
	