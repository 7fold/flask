import connexion
# from flask import Flask

app = connexion.FlaskApp(__name__, specification_dir="./")
app.add_api('swagger.yml')

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)