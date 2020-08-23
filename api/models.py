"""If you would want to have a one-to-one relationship you can pass uselist=False to relationship()."""
from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    rating = db.Column(db.Integer)
    awards = db.relationship('Award', lazy=True, backref='person', uselist=True) # loads MANY of type class Award


class Award(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(50), db.ForeignKey('movie.title'), nullable=False)
    award_name = db.Column(db.String(60))
