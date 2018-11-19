import os, mysql.connector
from typing import List, Dict
from flask import Flask, send_file, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (from the example template)"

@app.route("/test")
def main():
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)

@app.route("/lol")
def lol():
    return "Lol world!"

@app.route("/a")
def a():
    return "AAAA"

@app.route('/json')
def jsON():
    data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
    return jsonify(data)

def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'SomeStrongPassword123!',
        'host': 'mysql',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route("/db")
def index() -> str:
    return jsonify({'favorite_colors': favorite_colors()})


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
