# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, current_app


main = Blueprint("main", __name__)

@main.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":

    app = Flask(__name__)
    app.register_blueprint(main)

    app.run()
