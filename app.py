# Ioana A Mititean
# Exercise 24.3: REST and JSON
# Cupcakes

"""
Flask app for Cupcakes: route and view definitions.
"""

from flask import Flask, request, jsonify
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
    return (jsonify(cupcakes=serialized), 200)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """
    Get data about the single cupcake with the given ID, as JSON.
    """

    cupcake = db.get_or_404(Cupcake, cupcake_id)
    serialized = serialize_cupcake(cupcake)
    return (jsonify(cupcake=serialized), 200)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """
    Create a cupcake with flavor, size, rating and image data from the body of the request.

    Return the created cupcake as JSON.
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)
    return (jsonify(cupcake=serialized), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """
    Update the cupcake with flavor, size, rating and image data from the body of the request.

    Return the updated cupcake data as JSON.
    """

    cupcake = db.get_or_404(Cupcake, cupcake_id)
    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image = request.json["image"]

    db.session.commit()

    serialized = serialize_cupcake(cupcake)
    return (jsonify(cupcake=serialized), 200)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """
    Delete the cupcake with the given ID and return JSON indicating deletion success.
    """

    cupcake = db.get_or_404(Cupcake, cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(message="Deleted"), 200)

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
