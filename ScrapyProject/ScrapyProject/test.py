# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")  # take note of this decorator syntax, it's a common pattern
def hello():
    return "Hello World!"

@app.route("/test")  # take note of this decorator syntax, it's a common pattern
def test():
    return "Hello World!test"

if __name__ == "__main__":
    app.run()
