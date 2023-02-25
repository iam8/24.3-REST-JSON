# Ioana A Mititean
# Exercise 24.3: REST and JSON
# Cupcakes

"""
Flask app for Cupcakes: route and view definitions.
"""

from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config["SECRET_KEY"] = "O secreta secreta, of doamne"
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
# app.config['SQLALCHEMY_ECHO'] = True
