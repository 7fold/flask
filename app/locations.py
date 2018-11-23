from flask import jsonify, request
from config import db
from sqlalchemy import exc
from models import (Locations, LocationsSchema,
                    Products, DataSchema)
from datetime import datetime
import pytz


def get_all():
    pagination = db.session.query(
        Products.description,
        Locations.record_id,
        Locations.product_id,
        Locations.datetime,
        Locations.longitude,
        Locations.latitude,
        Locations.elevation
        ).join(
            Locations,
            Products._id ==
            Locations.product_id
            ).order_by(
                Locations.record_id
                ).paginate()
    sch = DataSchema(many=True)
    data = sch.dump(pagination.items).data

    return data


def read_one(record_id):
    loc = db.session.query(
        Products.description,
        Locations.record_id,
        Locations.product_id,
        Locations.datetime,
        Locations.longitude,
        Locations.latitude,
        Locations.elevation
        ).join(
            Locations,
            Products._id ==
            Locations.product_id
            ).filter(
                Locations.record_id ==
                record_id
                ).one_or_none()

    if loc is not None:
        sch = DataSchema()
        data = sch.dump(loc).data
        return data
    else:
        return jsonify({
            "detail": "record_id '{record_id}' not found".format(
                record_id=record_id
                ),
            "status": 404,
            "title": "Not found",
            "type": "about:blank"
        }), 404


def create(location):
    schema = LocationsSchema(many=False)
    new_location = schema.load(location, session=db.session).data

    try:
        db.session.add(new_location)
        db.session.commit()
        return jsonify({}), 201, {
            'Location': '{baseurl}/{id}'.format(baseurl=str(request.base_url),
                                                id=new_location.record_id)
        }
    except exc.IntegrityError:
        db.session().rollback()
        return jsonify({
            "detail": "product_id '{id}' do not exist".format(
                id=new_location.product_id
                ),
            "status": 400,
            "title": "Bad Request",
            "type": "about:blank"
        }), 400


def update(record_id, location):
    update_location = Locations.query.filter(
        Locations.record_id == record_id
    ).one_or_none()

    if update_location is not None:

        dt = datetime.utcnow()
        dt = dt.astimezone(pytz.timezone("America/Toronto"))

        update_location.product_id = location['product_id']
        update_location.latitude = location['latitude']
        update_location.longitude = location['longitude']
        update_location.elevation = location['elevation']
        update_location.datetime = dt

        db.session.commit()
        return jsonify({}), 200
    else:
        return jsonify({
            "detail": "record_id '{record_id}' not found".format(
                record_id=record_id
                ),
            "status": 404,
            "title": "Not found",
            "type": "about:blank"
        }), 404


def delete(record_id):
    location = Locations.query.filter(
        Locations.record_id ==
        record_id
        ).one_or_none()

    if location is not None:
        db.session.delete(location)
        db.session.commit()
        return jsonify({}), 200
    else:
        return jsonify({
            "detail": "record_id '{record_id}' not found".format(
                record_id=record_id
                ),
            "status": 404,
            "title": "Not found",
            "type": "about:blank"
        }), 404
