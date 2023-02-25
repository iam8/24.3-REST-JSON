# Ioana A Mititean
# Exercise 24.3: REST and JSON
# Cupcakes

"""
Seed file for Cupcakes app - adds initial data to database.
"""

from app import app, connect_db
from models import db, Cupcake

IMG1 = ("https://www.bakedbyrachel.com/wp-content/uploads/2018/01/"
        + "chocolatecupcakesccfrosting1_bakedbyrachel.jpg")


if __name__ == "__main__":

    connect_db(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create cupcakes
        c1 = Cupcake(flavor="cherry",
                     size="large",
                     rating=5)

        c2 = Cupcake(flavor="chocolate",
                     size="small",
                     rating=9,
                     image=IMG1)

        db.session.add_all([c1, c2])
        db.session.commit()
