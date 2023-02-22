from marshmallow import Schema, fields

from app.data_base import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre_scheme(Schema):
    id = fields.Int()
    name = fields.Str()
