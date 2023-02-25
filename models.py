# Ioana A Mititean
# Exercise 24.3: REST and JSON
# Cupcakes

"""
Models for Cupcake app.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    """
    Connect Flask app to SQLA database.
    """

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """
    Model for a cupcake.
    """

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(30), nullable=False)
    size = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, server_default=DEFAULT_IMG)
