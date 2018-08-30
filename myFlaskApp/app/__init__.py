from flask import Flask, render_template, flash, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "361f657555c5599857b926161b13403a"
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "cameronrtucker21@gmail.com"
app.config["MAIL_PASSWORD"] = "Waffles*11"
mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = "login"
loginManager.login_message_category = "danger"

from app import routes