# Ioana A Mititean
# Exercise 24.3: REST and JSON
# Cupcakes

"""
Flask app for Cupcakes: route and view definitions.
"""

from flask import Flask, redirect, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config["SECRET_KEY"] = "O secreta secreta, of doamne"
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
# app.config['SQLALCHEMY_ECHO'] = True


# ROUTES & VIEWS ----------------------------------------------------------------------------------

@app.route("/api/cupcakes")
def get_all_cupcakes():
    """
    Get data about all cupcakes, as JSON.
    """

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(cupcake) for cupcake in cupcakes]
    return jsonify(serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """
    Get data about the single cupcake with the given ID, as JSON.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)
    return jsonify(serialized)

# -------------------------------------------------------------------------------------------------


# HELPERS -----------------------------------------------------------------------------------------

def serialize_cupcake(cupcake):
    """
    Serialize a cupcake SQLAlchemy object to a Python dictionary.
    """

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

# -------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    connect_db(app)

    with app.app_context():
        db.create_all()

    app.run(host='127.0.0.1', port=5000, debug=True, threaded=False)
