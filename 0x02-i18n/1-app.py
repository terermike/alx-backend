#!/usr/bin/env python3
"""
Module documentation: This is a basic Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Function documentation: Renders the index.html template.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
