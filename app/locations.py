# System modules
import mysql.connector
from datetime import datetime
from typing import List, Dict


# 3rd party modules
from flask import make_response, abort, request

def db():
    config = {
            'user': 'root',
            'password': 'SomeStrongPassword123!',
            'host': 'mysql',
            'port': '3306',
            'database': 'texada'
        }
    return mysql.connector.connect(**config)

def get_all() -> List[Dict]:
    length = request.args.get('length')
    offset = request.args.get('offset')

    if length is not None and offset is None:
        limit = 'LIMIT {length}'.format(length=length)
    if offset is not None and length is None:
        limit = "LIMIT {offset},18446744073709551615".format(offset=offset)
    if offset is not None and length is not None:
        limit = 'LIMIT {offset},{length}'.format(offset=offset, length=length)
    else:
        limit = ''
    connection = db()
    cursor = connection.cursor()
    cursor.execute('SELECT t1.id as product_id, t2.record_id, t1.name as description, t2.datetime, t2.latitude, t2.longitude, t2.elevation from products t1 INNER JOIN locations t2 ON t1.id = t2.product_id {limit}'.format(limit=limit))
    RESULT = [{'product_id': product_id, 'record_id': record_id, 'description': description, 'datetime': datetime, 'latitude': latitude, 'longitude': longitude, 'elevation': elevation} for (product_id, record_id, description, datetime, latitude, longitude, elevation) in cursor]
    cursor.close()
    connection.close()

    return RESULT

def read_one(record_id) -> List[Dict]:

    connection = db()
    cursor = connection.cursor()
    cursor.execute('SELECT t2.record_id, t1.id as product_id, t1.name as description, t2.datetime, t2.latitude, t2.longitude, t2.elevation from products t1 INNER JOIN locations t2 ON t1.id = t2.product_id WHERE record_id = \'{record_id}\''.format(record_id=record_id))
    RESULT = [{'record_id': record_id, 'product_id': product_id, 'description': description, 'datetime': datetime, 'latitude': latitude, 'longitude': longitude, 'elevation': elevation} for (record_id, product_id, description, datetime, latitude, longitude, elevation) in cursor]

    cursor.close()
    connection.close()

    if len(RESULT) != 0:
        location = RESULT

    else:
        abort(
            404, "Location record with id: {record_id} not found".format(record_id=record_id)
        )

    return location

def create(location):

    product_id = location.get("product_id", None)
    latitude = location.get("latitude", None)
    longitude = location.get("longitude", None)
    elevation = location.get("elevation", None)

    if product_id is not None and latitude is not None and longitude is not None and elevation is not None:
        connection = db()
        cursor = connection.cursor()
        sql = "INSERT INTO locations (product_id, latitude, longitude, elevation) VALUES ({product_id}, {lat}, {lng}, {el})".format(product_id=product_id, lat=latitude, lng=longitude, el=elevation)
        cursor.execute(sql)
        connection.commit()
        return connection.commit(), 201

    else:
        abort(
            400,
            "An error occurred.",
        )

def update(record_id, location):

    connection = db()
    cursor = connection.cursor()
    cursor.execute('SELECT record_id FROM locations WHERE record_id = \'{record_id}\''.format(record_id=record_id))
    RESULT = [{'record_id': record_id} for (record_id) in cursor]

    cursor.close() 
    connection.close()

    if len(RESULT) != 0:
        product_id = location.get("product_id", None)
        latitude = location.get("latitude", None)
        longitude = location.get("longitude", None)
        elevation = location.get("elevation", None)
        if product_id is not None and latitude is not None and longitude is not None and elevation is not None:
            connection = db()
            cursor = connection.cursor()
            sql = 'UPDATE locations SET product_id = \'{product_id}\', latitude = \'{latitude}\', longitude = \'{longitude}\', elevation = \'{elevation}\' WHERE record_id = \'{record_id}\''.format(product_id=product_id, latitude=latitude, longitude=longitude, elevation=elevation, record_id=record_id)
            cursor.execute(sql)
            connection.commit()
            return connection.commit(), 200

    else:
        abort(
            404, "Location with id: {record_id} not found".format(record_id=record_id)
        )


def delete(record_id):

    connection = db()
    cursor = connection.cursor()
    cursor.execute('SELECT record_id FROM locations WHERE record_id = \'{record_id}\''.format(record_id=record_id))
    RESULT = [{'record_id': record_id} for (record_id) in cursor]

    cursor.close() 
    connection.close()

    if len(RESULT) != 0:
        connection = db()
        cursor = connection.cursor()
        sql = 'DELETE FROM locations WHERE record_id = \'{record_id}\''.format(record_id=record_id)
        cursor.execute(sql)
        connection.commit()
        return connection.commit(), 200

    else:
        abort(
            404, "Location with id: {record_id} not found".format(record_id=record_id)
        )
