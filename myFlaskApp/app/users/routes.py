from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.database import User, Review
from app.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from app.users.utils import savePicture, sendResetEmail, id_generator


users = Blueprint("users", __name__)

@users.route("/register", methods = ["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("main.home"))
	form = RegistrationForm()
	if form.validate_on_submit():
		userName = User.query.filter_by(username = form.username.data).first()
		userEmail = User.query.filter_by(email = form.email.data).first()
		if userName:
			flash("Username already exists. Please try again", "danger")
		elif userEmail:
			flash("Email already exists. Please try again", "danger")
		else:
			hashed_password = bcrypt.generate_password_hash(form.password.data)
			user = User(username = form.username.data.lower(), email = form.email.data.lower(), password = hashed_password)
			db.session.add(user)
			db.session.commit()
			flash("Your account has been created! Please sign in!", "success")
			return redirect(url_for("users.login"))
	return render_template("register.html", form = form)

@users.route("/login", methods = ["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("main.home"))
	form = LoginForm()
	if form.validate_on_submit():
		userEmail = User.query.filter_by(email = form.email.data.lower()).first()
		if not userEmail:
			flash("Username does not exist. Please try again", "danger")
		elif not bcrypt.check_password_hash(userEmail.password, form.password.data):
			flash("Incorrect password. Please try again", "danger")
		else:
		 	login_user(userEmail, remember = form.remember.data)
		 	next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for("main.home"))
	return render_template("login.html", form = form)

@users.route("/reset_password", methods = ["GET", "POST"])
def reset_request():
	if current_user.is_authenticated:
		return redirect(url_for("main.home"))
	form = RequestResetForm()
	if form.validate_on_submit():
		user = user.query.filter_by(email = form.email.data).first()
		sendResetEmail(user)
		flash("An email to reset your password has been sent to your email!", "success")
		return redirect(url_for("users.login"))
	return render_template("reset_request.html", form = form)

@users.route("/reset_password/<token>", methods = ["GET", "POST"])
def reset_token(token):
	if current_user.is_authenticated:
		return redirect(url_for("home"))
	user = user.verify_reset_token(token)
	if not user:
		flash("Token enter is invalid or has expired!", "danger")
		return redirect(url_for("users.reset_request"))
	form = ResetPasswordForm()
	if form.validate_on_submit():
			hashed_password = bcrypt.generate_password_hash(form.password.data)
			user.password = hashed_password
			db.session.commit()
			flash("Your password has been updated! Please sign in!", "success")
			return redirect(url_for("users.login"))
	return render_template("reset_token.html", form = form)

@users.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("main.home"))

@users.route("/account")
@login_required
def account():
	return render_template("account.html")

@users.route("/edit_account", methods = ["GET", "POST"])
@login_required
def edit_account():
	print current_user.image_file
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.profilePicture.data:
			newPicture = savePicture(form.profilePicture.data)
			current_user.image_file = newPicture
		current_user.username = form.username.data.lower()
		current_user.email = form.email.data.lower()
		db.session.commit()
		flash("Your account changes have been saved!", "success")
		return redirect(url_for("users.account"))
	elif request.method == "GET":
		form.username.data = current_user.username
		form.email.data = current_user.email
	return render_template("edit_account.html", form = form)

@users.route("/user/<string:username>")
def user_reviews(username):
	page = request.args.get("page", 1, type = int)
	user = User.query.filter_by(username = username).first_or_404()
	reviews = Review.query.filter_by(author = user).order_by(Review.date_posted.desc()).paginate(page = page, per_page = 5)
	return render_template("user_reviews.html", reviews = reviews, user = user)