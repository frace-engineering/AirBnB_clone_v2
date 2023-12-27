#!/usr/bin/python3
"""Python script that starts a web application """
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display "Hello HBNB!" on the browser"""
    return "Hello HBNB!"


if __name__ == "__main__":
    ""' Run the app on port 5000 and all host """
    app.run(host='0.0.0.0', port=5000)
