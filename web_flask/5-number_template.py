#!/usr/bin/python3
"""Python script that starts a web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display "Hello HBNB!" on the browser"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display "HBNB!" on the browser"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Display "C {text}" on the browser"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_text(text='is cool'):
    """ Display "Python {text}" on the browser"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Display "{n} is a number" on the browser"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display html template with "Number: {n} on the browser"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    """ Run the app on port 5000 and all host """
    app.run(host='0.0.0.0', port=5000)
