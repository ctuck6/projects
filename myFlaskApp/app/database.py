from datetime import datetime
from app import db, loginManager
from flask_login import UserMixin

@loginManager.user_loader
def loadUser(userId):
	return User.query.get(int(userId))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    image_file = db.Column(db.String(20), unique = False, nullable = False, default = "default.jpeg")
    password = db.Column(db.String(20), nullable = False)
    reviews = db.relationship("Review", backref = "author", lazy = True)

    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    body = db.Column(db.Text, nullable = False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return "Review('{}', '{}')".format(self.title, self.date_posted)