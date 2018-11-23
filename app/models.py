from datetime import datetime
from config import db, ma
from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property
import pytz


dt = datetime.utcnow()
dt = dt.astimezone(pytz.timezone("America/Toronto"))


class Products(db.Model):
    __tablename__ = "products"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)

    def __init__(self, name):
        self.start = name

    @hybrid_property
    def description(self):
        return self.name


class ProductsSchema(ma.ModelSchema):
    class Meta:
        model = Products
        sqla_session = db.session


class Locations(db.Model):
    __tablename__ = "locations"
    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, default=dt,
                         onupdate=dt, nullable=False)
    longitude = db.Column(db.Float(precision='10,7', asdecimal=False,
                          decimal_return_scale=False), nullable=False)
    latitude = db.Column(db.Float(precision='10,7', asdecimal=False,
                         decimal_return_scale=False), nullable=False)
    elevation = db.Column(db.Integer, nullable=False)


class LocationsSchema(ma.ModelSchema):
    class Meta:
        model = Locations
        sqla_session = db.session


class DataSchema(ma.Schema):
    product_id = fields.Integer()
    record_id = fields.Integer()
    description = fields.Str()
    datetime = fields.Date()
    latitude = fields.Float()
    longitude = fields.Float()
    elevation = fields.Integer()
