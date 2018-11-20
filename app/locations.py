import mysql.connector as mysql
from typing import List, Dict
from flask import abort, request


def db(sql, commit):
    config = {
        'user': 'root',
        'password': 'SomeStrongPassword123!',
        'host': 'mysql',
        'port': '3306',
        'database': 'texada'
    }
    connection = mysql.connect(**config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        if commit is True:
            return connection.commit()
        else:
            return cursor.fetchall()
    except Exception:
        pass
    finally:
        cursor.close()
        connection.close()


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def get_all() -> List[Dict]:
    limit = request.args.get('limit')
    page = request.args.get('page')

    if limit is not None and page is not None:
        offset = (num(page) - 1) * num(limit)
        sql = 'SELECT \
        t1.id as product_id, t2.record_id, \
        t1.name as description, t2.datetime, \
        t2.latitude, t2.longitude, t2.elevation \
        FROM products t1 INNER JOIN locations t2 \
        ON t1.id = t2.product_id \
        LIMIT {limit} OFFSET {offset}'.format(offset=offset, limit=limit)
    else:
        sql = 'SELECT \
        t1.id as product_id, t2.record_id, \
        t1.name as description, t2.datetime, \
        t2.latitude, t2.longitude, t2.elevation \
        FROM products t1 INNER JOIN locations t2 \
        ON t1.id = t2.product_id'

    data = db(sql, False)
    RESULT = [
        {
            'product_id': product_id,
            'record_id': record_id,
            'description': description,
            'datetime': datetime,
            'latitude': latitude,
            'longitude': longitude,
            'elevation': elevation
        }
        for (product_id, record_id,
             description, datetime,
             latitude, longitude,
             elevation) in data]

    return RESULT


def read_one(record_id) -> List[Dict]:

    sql = 'SELECT \
    t2.record_id, t1.id as product_id, \
    t1.name as description, t2.datetime, \
    t2.latitude, t2.longitude, t2.elevation \
    FROM products t1 INNER JOIN locations t2 \
    ON t1.id = t2.product_id \
    WHERE record_id =\'{record_id}\''.format(record_id=record_id)
    data = db(sql, False)
    RESULT = [
        {
            'record_id': record_id,
            'product_id': product_id,
            'description': description,
            'datetime': datetime,
            'latitude': latitude,
            'longitude': longitude,
            'elevation': elevation
        }
        for (record_id, product_id,
             description, datetime,
             latitude, longitude,
             elevation) in data]

    if len(RESULT) != 0:
        location = RESULT

    else:
        abort(
            404, "Location record with id: {record_id} \
            not found".format(record_id=record_id)
        )

    return location


def create(location):

    product_id = location.get("product_id", None)
    latitude = location.get("latitude", None)
    longitude = location.get("longitude", None)
    elevation = location.get("elevation", None)

    if (product_id is not None and latitude is not None
            and longitude is not None and elevation is not None):
        sql = "INSERT INTO locations \
        (product_id, latitude, longitude, elevation) VALUES \
        ({product_id}, {lat}, {lng}, {el})".format(product_id=product_id,
                                                   lat=latitude, lng=longitude,
                                                   el=elevation)
        return db(sql, True), 201

    else:
        abort(
            400,
            "An error occurred.",
        )


def update(record_id, location):

    sql = 'SELECT record_id FROM locations \
    WHERE record_id = \'{record_id}\''.format(record_id=record_id)
    data = db(sql, False)
    RESULT = [{'record_id': record_id} for (record_id) in data]

    if len(RESULT) != 0:
        product_id = location.get("product_id", None)
        latitude = location.get("latitude", None)
        longitude = location.get("longitude", None)
        elevation = location.get("elevation", None)
        if (product_id is not None and latitude is not None
                and longitude is not None and elevation is not None):
            query = 'UPDATE locations \
            SET product_id = \'{product_id}\', latitude = \'{latitude}\', \
            longitude = \'{longitude}\', elevation = \'{elevation}\' \
            WHERE record_id = \'{record_id}\'\
            '.format(product_id=product_id, latitude=latitude,
                     longitude=longitude, elevation=elevation,
                     record_id=record_id)
            return db(query, True), 200

    else:
        abort(
            404, "Location with id: {record_id} \
            not found".format(record_id=record_id)
        )


def delete(record_id):

    sql = 'SELECT record_id FROM locations WHERE \
    record_id = \'{record_id}\''.format(record_id=record_id)
    data = db(sql, False)
    RESULT = [{'record_id': record_id} for (record_id) in data]

    if len(RESULT) != 0:
        query = 'DELETE FROM locations \
        WHERE record_id = \'{record_id}\''.format(record_id=record_id)
        return db(query, True), 200

    else:
        abort(
            404, "Location with id: {record_id} \
            not found".format(record_id=record_id)
        )
