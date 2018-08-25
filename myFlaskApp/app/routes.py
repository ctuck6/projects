from flask import render_template, flash, request, url_for, redirect
from app import app, db, bcrypt
from app.database import User
from app.data import Reviews, Users
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required

Reviews = Reviews()
Users = Users()

@app.route('/')
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/reviews")
def reviews():
	return render_template("reviews.html", reviews = Reviews)

@app.route("/register", methods = ["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("home"))
	form = RegistrationForm()
	if form.validate_on_submit():
		userName = User.query.filter_by(username=form.username.data).first()
		userEmail = User.query.filter_by(email=form.email.data).first()
		if userName:
			flash("Username already exists. Please try again", "danger")
		elif userEmail:
			flash("Email already exists. Please try again", "danger")
		else:
			hashed_password = bcrypt.generate_password_hash(form.password.data)
			user = User(username=form.username.data, email=form.email.data, password=hashed_password)
			db.session.add(user)
			db.session.commit()
			flash("Your account has been created! Please sign in!", "success")
			return redirect(url_for("login"))

	flash("Registration failed. Please try again", "danger")
	return render_template("register.html", title="Register", form=form)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("home"))
	form = LoginForm()
	if form.validate_on_submit():
		userEmail = User.query.filter_by(email=form.email.data).first()
		if not userEmail:
			flash("Username does not exist. Please try again", "danger")
		elif not bcrypt.check_password_hash(userEmail.password, form.password.data):
			flash("Incorrect password. Please try again", "danger")
		else:
		 	login_user(userEmail, remember=form.remember.data)
		 	next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for("home"))
	return render_template("login.html", title="Login", form=form)

@app.route("/review/<string:id>/")
def review(id):
	return render_template("review.html", id = id)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
	return render_template("account.html", title="Account")