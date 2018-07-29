from flask import Flask, render_template
from data import Reviews

app = Flask(__name__)

Reviews = Reviews()

@app.route('/')
def index():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/reviews")
def reviews():
	return render_template("reviews.html", reviews = Reviews)

@app.route("/review/<string:id>/")
def review(id):
	return render_template("review.html", id = id)

if __name__ == "__main__":
	app.run(debug = True)