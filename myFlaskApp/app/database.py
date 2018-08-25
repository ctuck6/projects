from datetime import datetime
from app import db, loginManager
from flask_login import UserMixin

@loginManager.user_loader
def loadUser(userId):
	return User.query.get(int(userId))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    image_file = db.Column(db.String(20), unique = False, nullable = False, default = "default.jpeg")
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)