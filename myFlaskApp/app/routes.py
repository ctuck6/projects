from flask import render_template, flash, request, url_for, redirect, abort
from app import app, db, bcrypt
from app.database import User, Review
from app.createdFunctions import id_generator, savePicture
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, ReviewForm
from flask_login import login_user, logout_user, current_user, login_required
import ast

@app.route('/')
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/reviews", methods = ["GET", "POST"])
def reviews():
	page = request.args.get("page", 1, type=int)
	reviews = Review.query.order_by(Review.date_posted.desc()).paginate(page = page, per_page = 5)
	return render_template("reviews.html", reviews = reviews)

@app.route("/review/<int:review_id>")
def review(review_id):
	review = Review.query.get_or_404(review_id)
	return render_template("review.html", review = review)

@app.route("/review/<int:review_id>/update",  methods = ["GET", "POST"])
@login_required
def update_review(review_id):
	review = Review.query.get_or_404(review_id)
	if review.author != current_user:
		abort(403)
	form = ReviewForm()
	if form.validate_on_submit():
		review.title = form.title.data
		review.body = form.body.data
		db.session.commit()
		flash("Your post has been updated!", "success")
		return redirect(url_for("review", review_id = review.id))
	elif request.method == "GET":
		form.title.data = review.title
		form.body.data = review.body
	return render_template("create_review.html", legend = "Update Review", form = form)

@app.route("/review/<int:review_id>/delete",  methods = ["POST"])
@login_required
def delete_review(review_id):
	review = Review.query.get_or_404(review_id)
	if review.author != current_user:
		abort(403)
	db.session.delete(review)
	db.session.commit()
	flash("Your post has been deleted!", "success")
	return redirect(url_for("reviews"))

@app.route("/review/new", methods = ["GET", "POST"])
@login_required
def new_review():
	form = ReviewForm()
	if form.validate_on_submit():
		review = Review(title = form.title.data, body = form.body.data, author = current_user)
		db.session.add(review)
		db.session.commit()
		flash("Your review has been posted!", "success")
		return redirect(url_for("reviews"))
	return render_template("create_review.html", legend = "New Review", form = form)

@app.route("/register", methods = ["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for("home"))
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
			return redirect(url_for("login"))
	return render_template("register.html", form = form)

@app.route("/login", methods = ["GET", "POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for("home"))
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
			return redirect(next_page) if next_page else redirect(url_for("home"))
	return render_template("login.html", form = form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
	return render_template("account.html")

@app.route("/edit_account", methods = ["GET", "POST"])
@login_required
def edit_account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.profilePicture.data:
			newPicture = savePicture(form.profilePicture.data)
			current_user.image_file = newPicture
		current_user.username = form.username.data.lower()
		current_user.email = form.email.data.lower()
		db.session.commit()
		flash("Your account changes have been saved!", "success")
		return redirect(url_for("account"))
	elif request.method == "GET":
		form.username.data = current_user.username
		form.email.data = current_user.email
	return render_template("edit_account.html", form = form)

@app.route("/user/<string:username>")
def user_reviews(username):
	page = request.args.get("page", 1, type = int)
	user = User.query.filter_by(username = username).first_or_404()
	reviews = Review.query.filter_by(author = user).order_by(Review.date_posted.desc()).paginate(page = page, per_page = 5)
	return render_template("user_reviews.html", reviews = reviews, user = user)

@app.route("/latest_reviews", methods = ["GET", "POST"])
def latest_reviews():
	reviews = Review.query.order_by(Review.date_posted.desc()).paginate(page = 1, per_page = 10)
	return render_template("latest_reviews.html", reviews = reviews)
