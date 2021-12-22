import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")   # template to display on root folder
def index():
    '''
    renders index.html
    '''
    return render_template("index.html")


@app.route("/about")
def about():
    '''
    renders about page
    '''
    return render_template("about.html")


@app.route("/contact")
def contact():
    '''
    renders contact page
    '''
    return render_template("contact.html")


@app.route("/careers")
def careers():
    '''
    renders careers page
    '''
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
