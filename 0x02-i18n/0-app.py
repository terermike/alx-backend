#!/usr/bin/env python3
"""
Module documentation: This is a basic Flask app.
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    """
    Function documentation: Renders the index.html template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
