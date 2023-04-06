from flask import Flask
from flask import render_template

new = Flask(__name__)

@new.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    new.run(debug=True)