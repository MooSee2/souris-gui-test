from .server import db


class reservoir(db.Model):
    __tablename__ = "reservoir"

    datetime = db.Column(db.String, primary_key=True)
    discharge = db.Column(db.Float)
