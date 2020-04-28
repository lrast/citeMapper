# url routing logic

from flask import render_template
from webapp import app


@app.route('/')
def home():
    return render_template("home.html")


