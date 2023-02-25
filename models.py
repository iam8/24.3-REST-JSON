# Ioana A Mititean
# Exercise 24.3: REST and JSON
# Cupcakes

"""
Models for Cupcake app.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """
    Connect Flask app to SQLA database.
    """

    db.app = app
    db.init_app(app)
