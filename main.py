from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/income/<name>")
def get_income_type(name):
    return "name: {}".format(name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')